"""Read-only balance-analysis CLI: computes derived-stat progression curves
(HP, Evasion, AR, attack bonus, spell modifier, ...) for each archetype in
data/builds/*.yaml across levels 1-12, using the formulas in formulas.py.

Never writes into core/ - this is an analysis tool, not part of the content
generation pipeline (that's scripts/build.py).
"""

import argparse
import csv
import io
import json
import sys
from pathlib import Path

import formulas
from build_models import Archetype, check_archetype_budget
from loaders import DATA_DIR, REPO_ROOT, SPELL_FILES, load_data, load_yaml
from progression_models import ProgressionTable

BUILDS_DIR = DATA_DIR / "builds"
CORE_OUTPUT_DIR = REPO_ROOT / "core"

ARCANE_SCHOOLS = {s.lower() for s in SPELL_FILES["arcane"]}

# Skill Categories table, core_rules.md:113-132 - which attribute governs each
# skill, used to resolve each attribute's Ward (formulas.ward_dc: 5 + Attribute
# + highest Skill under that Attribute).
SKILL_CATEGORIES = {
    "STR": ["One-Handed Blades", "Two-Handed Blades", "Axes & Hammers", "Polearms",
            "Brawling", "Slings & Whips"],
    "REF": ["Rapiers & Fencing", "Daggers & Knives", "Bows & Crossbows", "Thrown Weapons",
            "Pistols", "Long Guns", "Heavy Firearms"],
    "END": ["Athletics", "Armorer", "Survival", "Shields", "Riding"],
    "DEX": ["Agility", "Acrobatics", "Stealth", "Lockpicking", "Sleight of Hand", "Crafting",
            "Perception"],
    "MIND": ["Alchemy", "Enchanting", "Spell Crafting", "Historic Lore", "Medical Lore",
              "Nature Lore", "Identify"],
    "ARC": ["Arcane Lore", "Aeromancy", "Geomancy", "Hydromancy", "Pyromancy", "Shadowmancy"],
    "FAI": ["Religious Lore", "Benediction", "Invocation", "Necration", "Cultivation", "Subjugation"],
    "CHA": ["Persuasion", "Deception", "Intimidation", "Leadership", "Animal Handling",
            "Insight", "Performance"],
}


def average_ward(snapshot) -> float:
    """A single-number defensive benchmark: the archetype's Ward (formulas.ward_dc)
    averaged across all 8 attributes, using its highest rank in that attribute's
    skill category. A real Spell Overcome targets one specific attribute's Ward
    (the spell says which) - this is a general 'how hard am I to affect with
    magic overall' stand-in, not any single spell's actual target DC."""
    wards = []
    for attribute, skills in SKILL_CATEGORIES.items():
        best_skill = max((snapshot.skills.get(name, 0) for name in skills), default=0)
        wards.append(formulas.ward_dc(snapshot.attributes[attribute], best_skill))
    return sum(wards) / len(wards)


def load_progression() -> ProgressionTable:
    raw = load_yaml(DATA_DIR / "progression.yaml")
    return ProgressionTable(**raw)


def load_archetypes() -> dict[str, Archetype]:
    archetypes = {}
    for path in sorted(BUILDS_DIR.glob("*.yaml")):
        archetype = Archetype(**load_yaml(path))
        archetypes[archetype.key] = archetype
    return archetypes


def build_weapon_index(weapons) -> dict:
    index = {}
    for kind_ns in (weapons.melee, weapons.ranged, weapons.firearms):
        for block in vars(kind_ns).values():
            for w in block.weapons:
                index[w.name] = w
    return index


def build_armor_index(armor) -> dict:
    index = {}
    for block in vars(armor.armor).values():
        for a in block.armors:
            index[a.name] = a
    return index


def build_shield_index(armor) -> dict:
    return {s.name: s for s in armor.shields}


def compute_stats(archetype, snapshot, weapon_index, armor_index, shield_index) -> dict:
    attrs = snapshot.attributes
    stats = {
        "hp": formulas.hp(attrs["END"]),
        "carrying_capacity": formulas.carrying_capacity(attrs["END"], attrs["STR"]),
    }

    weapon = weapon_index[snapshot.equipment.weapon]
    armor_entry = armor_index[snapshot.equipment.armor] if snapshot.equipment.armor else None
    shield_entry = shield_index[snapshot.equipment.shield] if snapshot.equipment.shield else None

    def penalty_magnitude(entry) -> int:
        # data/armor/*.yaml and data/armor/shields.yaml store `penalty` as a
        # negative number (e.g. -4); formulas.effective_armor_penalty() wants
        # a non-negative magnitude.
        return abs(entry.penalty) if entry is not None and entry.penalty else 0

    base_penalty = penalty_magnitude(armor_entry) + penalty_magnitude(shield_entry)
    effective_penalty = formulas.effective_armor_penalty(base_penalty, snapshot.armorer_ranks)

    stats["evasion"] = formulas.evasion(snapshot.agility_skill, attrs["DEX"], effective_penalty)
    stats["dodge"] = formulas.dodge(stats["evasion"])
    stats["max_dodges_per_short_rest"] = formulas.max_dodges_per_short_rest(attrs["DEX"])
    stats["initiative_bonus"] = formulas.initiative_bonus(attrs["REF"], attrs["DEX"])

    weapon_skill_rank = snapshot.skills.get(archetype.weapon_skill, 0)
    weapon_attr_value = attrs[snapshot.equipment.weapon_attribute]
    stats["attack_bonus"] = formulas.attack_bonus(weapon_skill_rank, weapon_attr_value)
    # target_ar=0: this is the attacker's own pre-mitigation damage output,
    # not resolved against any specific opponent's AR.
    stats["average_damage"] = formulas.dice_average(weapon.damage) + formulas.damage_bonus(weapon_attr_value, 0)
    stats["armor_rating"] = formulas.armor_rating(
        armor_entry.ar if armor_entry else None,
        shield_entry.ar_bonus if shield_entry else 0,
    )

    if archetype.school_skill is not None:
        stats["mana_pool"] = formulas.mana_pool(attrs["MIND"])
        school_rank = snapshot.skills.get(archetype.school_skill, 0)
        casting_attr = attrs["ARC"] if archetype.school_skill.lower() in ARCANE_SCHOOLS else attrs["FAI"]
        stats["spell_modifier"] = formulas.spell_modifier(school_rank, casting_attr, effective_penalty)

    # The bonus this archetype actually rolls to hit with: Spell Modifier for a
    # caster (spell attacks roll 1d12 + Spell Modifier vs. Evasion too, per
    # magic_overview.md:49 - same target stat as a weapon attack), weapon
    # Attack Bonus otherwise.
    stats["primary_offense_bonus"] = stats["spell_modifier"] if archetype.school_skill is not None else stats["attack_bonus"]

    stats["average_ward"] = average_ward(snapshot)

    return stats


def parse_levels(spec: str) -> list[int]:
    if "-" in spec:
        lo, hi = spec.split("-", 1)
        return list(range(int(lo), int(hi) + 1))
    return [int(spec)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--format", choices=["csv", "json"], default="csv")
    parser.add_argument("--out", type=Path, default=None, help="write to this file instead of stdout")
    parser.add_argument("--levels", default="1-12", help="e.g. '1-12' or '5'")
    parser.add_argument("--archetype", nargs="+", default=None, help="restrict to these archetype keys")
    args = parser.parse_args()

    if args.out is not None:
        resolved = args.out.resolve()
        if resolved == CORE_OUTPUT_DIR or CORE_OUTPUT_DIR in resolved.parents:
            parser.error(
                f"--out must not write into {CORE_OUTPUT_DIR} - this is a read-only "
                f"analysis tool, not part of the core/ content generation pipeline"
            )

    levels = parse_levels(args.levels)
    progression = load_progression()
    archetypes = load_archetypes()

    if args.archetype:
        unknown = set(args.archetype) - archetypes.keys()
        if unknown:
            parser.error(
                f"unknown archetype(s): {', '.join(sorted(unknown))}. "
                f"Known: {', '.join(sorted(archetypes))}"
            )
        archetypes = {k: v for k, v in archetypes.items() if k in args.archetype}

    for archetype in archetypes.values():
        for warning in check_archetype_budget(archetype, progression):
            print(f"warning: {warning}", file=sys.stderr)

    weapons, armor = load_data()
    weapon_index = build_weapon_index(weapons)
    armor_index = build_armor_index(armor)
    shield_index = build_shield_index(armor)

    rows = []
    for archetype in archetypes.values():
        for level in levels:
            snapshot = archetype.snapshot(level)
            stats = compute_stats(archetype, snapshot, weapon_index, armor_index, shield_index)
            for stat, value in stats.items():
                rows.append({"archetype": archetype.key, "level": level, "stat": stat, "value": value})

    if args.format == "json":
        output = json.dumps(rows, indent=2)
    else:
        buf = io.StringIO()
        writer = csv.DictWriter(buf, fieldnames=["archetype", "level", "stat", "value"])
        writer.writeheader()
        writer.writerows(rows)
        output = buf.getvalue()

    if args.out is not None:
        args.out.write_text(output, encoding="utf-8")
        print(f"wrote {args.out}", file=sys.stderr)
    else:
        print(output, end="" if args.format == "csv" else "\n")


if __name__ == "__main__":
    main()

"""Derived-stat math mirrored from the rulebook prose.

This is the single source of truth used by scripts/balance_report.py to compute
combat/derived-stat curves. Each "book formula" function's docstring cites the
exact source line it mirrors - when a rule changes in the prose, grep for that
citation to find what to update here (and vice versa). These files are NOT
regenerated from this module; core_rules.md, combat.md, and magic_overview.md
stay hand-authored, since they are ~90% narrative prose with formulas scattered
throughout, unlike the clean tabular data that weapons/armor/progression
generate from.
"""

import re
from typing import Optional

# --- Book formulas -----------------------------------------------------------


def hp(end: int) -> int:
    """Maximum HP = (END x 3) + 10.
    Mirrors core_rules.md:103, character_creation.md:94."""
    return end * 3 + 10


def mana_pool(mind: int) -> int:
    """Maximum Mana = MIND x 2.
    Mirrors magic_overview.md:18, character_creation.md:95."""
    return mind * 2


def carrying_capacity(end: int, str_: int, size_multiplier: float = 1.0) -> float:
    """Carrying Capacity = ((END + STR) x 10) + 10 lbs, x size multiplier.
    Mirrors core_rules.md:151 (base formula) and the size table at
    core_rules.md:157-163 (size_multiplier)."""
    return ((end + str_) * 10 + 10) * size_multiplier


def effective_armor_penalty(base_penalty: int, armorer_ranks: int) -> int:
    """Each 2 ranks in Armorer reduces Armor Penalty toward 0 by 1.
    Mirrors combat.md:117, magic_overview.md:33.
    base_penalty is a non-negative magnitude (points subtracted from Evasion/
    spell rolls, e.g. 4 for a -4 armor penalty) - NOTE data/armor/*.yaml
    stores `penalty` as a negative number; callers must negate/abs() it
    before passing it in here. The result never goes below 0."""
    return max(0, base_penalty - armorer_ranks // 2)


def evasion(agility_skill: int, dex: int, armor_penalty: int) -> int:
    """Evasion = 5 + Agility + DEX - Armor Penalty.
    Mirrors combat.md:84, character_creation.md:97.
    NOTE: 'Agility' is the DEX-governed *skill* of that name (Combat Skills
    table, core_rules.md:118), not a distinct attribute - agility_skill is a
    skill rank (0-10), dex is the DEX attribute score, kept as separate
    parameters deliberately."""
    return 5 + agility_skill + dex - armor_penalty


def dodge(evasion_value: int) -> int:
    """Dodge = Evasion + 5.
    Mirrors character_creation.md:98. Does not appear in core_rules.md/combat.md."""
    return evasion_value + 5


def max_dodges_per_short_rest(dex: int) -> int:
    """Max Dodges/Short Rest = DEX / 2, rounded down.
    Mirrors character_creation.md:99."""
    return dex // 2


def initiative_bonus(ref: int, dex: int) -> int:
    """Static bonus added to 1d12 for Initiative: (REF + DEX) / 2, rounded down.
    Mirrors combat.md:9, character_creation.md:100."""
    return (ref + dex) // 2


def attack_bonus(weapon_skill: int, attribute: int) -> int:
    """Static bonus added to 1d12 for an attack roll vs. target's Evasion.
    Mirrors combat.md:41,43 (Attack Roll + Trained: Attribute only applies
    once weapon_skill >= 1)."""
    return weapon_skill + attribute if weapon_skill >= 1 else weapon_skill


def damage_bonus(attribute: int, target_ar: int) -> int:
    """Static addend to weapon damage dice: Weapon Damage + Attribute - target's AR.
    Mirrors combat.md:44. Caller supplies the weapon's dice-average separately
    via dice_average() below - this function only owns the +Attribute -AR part."""
    return attribute - target_ar


def skill_check_bonus(skill_ranks: int, attribute: int) -> int:
    """Static bonus added to 1d12 for a Skill Check.
    Mirrors core_rules.md:72,75 (Skill Check Formula + Trained: Attribute
    only applies once skill_ranks >= 1)."""
    return skill_ranks + attribute if skill_ranks >= 1 else skill_ranks


def ward_dc(attribute: int, best_governed_skill: int) -> int:
    """Ward DC = 5 + Attribute + highest Skill under that Attribute.
    This is the static DC that Spell Overcomes (and other effects) roll against.
    Mirrors magic_overview.md:57."""
    return 5 + attribute + best_governed_skill


def spell_modifier(school_skill: int, casting_attribute: int, armor_penalty: int) -> int:
    """Spell Modifier = Magic School Skill + ARC or FAI - Armor Penalty.
    This is the single static bonus added to 1d12 for both Spell Attacks
    (vs. target's Evasion, magic_overview.md:49) and Spell Overcomes
    (vs. target's Ward, magic_overview.md:55). Mirrors magic_overview.md:43,45
    (Spell Modifier + Trained: ARC/FAI only applies once school_skill >= 1)."""
    trained_attribute = casting_attribute if school_skill >= 1 else 0
    return school_skill + trained_attribute - armor_penalty


# --- Utility helpers (not cited rules - engineering scaffolding) -------------

D12_AVERAGE = 6.5  # expected value of 1d12, for expected-value curve calculations

_DICE_RE = re.compile(r"(\d+)d(\d+)(?:\s*\\?([+-])\s*(\d+))?")


def dice_average(expr: str) -> float:
    """Parse a dice-notation string such as '1d6 Piercing', '2d4 Slashing', or
    '1d6 \\+ 1 Piercing' (a flat modifier on the dice, escaped per this repo's
    Markdown-special-character convention) and return the expected value of
    the dice-plus-modifier portion (ignores damage-type words and any other
    trailing text). Used to turn the free-text `damage` strings from
    data/weapons/*.yaml into a number for balance_report.py. Not itself a
    cited rule - general dice math."""
    match = _DICE_RE.search(expr)
    if not match:
        raise ValueError(f"Could not parse dice notation from {expr!r}")
    count, sides, sign, flat = match.groups()
    average = int(count) * (int(sides) + 1) / 2
    if flat is not None:
        average += int(flat) if sign == "+" else -int(flat)
    return average


def armor_rating(base_ar: Optional[int], shield_ar_bonus: int = 0) -> int:
    """AR is not itself a formula - it's a flat stat looked up from equipped
    gear (ArmorEntry.ar / ShieldEntry.ar_bonus in models.py). This just sums
    armor + shield, treating a missing/None armor AR as 0."""
    return (base_ar or 0) + shield_ar_bonus

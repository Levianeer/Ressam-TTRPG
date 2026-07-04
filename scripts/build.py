import argparse
import difflib
import re
import sys
from pathlib import Path
from types import SimpleNamespace

import yaml
from jinja2 import Environment, FileSystemLoader
from pydantic import ValidationError

from models import AmmoEntry, ArmorBlock, ShieldEntry, UnarmedEntry, WeaponBlock
from spell_models import SpellEntry
from feat_models import FeatSubcategory, PrestigeFeatEntry

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
TEMPLATES_DIR = REPO_ROOT / "templates"
OUTPUT_DIR = REPO_ROOT / "core" / "equipment"
MAGIC_OUTPUT_DIR = REPO_ROOT / "core" / "magic"
FEATS_OUTPUT_DIR = REPO_ROOT / "core" / "feats"

SPELL_FILES = {
    "arcane": {
        "aeromancy": 6, "geomancy": 6, "hydromancy": 6, "pyromancy": 6, "shadowmancy": 7,
    },
    "divine": {
        "benediction": 6, "cultivation": 6, "invocation": 6, "necration": 6, "subjugation": 6,
    },
}


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def check_duplicate_names(names: list[str], where: str):
    seen = set()
    for name in names:
        if name in seen:
            raise SystemExit(f"Duplicate entry name '{name}' in {where}")
        seen.add(name)


def load_weapon_file(path: Path, kind: str) -> dict[str, WeaponBlock]:
    raw = load_yaml(path)
    blocks = {}
    for key, block_data in raw.items():
        block = WeaponBlock(kind=kind, **block_data)
        check_duplicate_names([w.name for w in block.weapons], f"{path.name}/{key}")
        blocks[key] = block
    return blocks


def load_data():
    melee = load_weapon_file(DATA_DIR / "weapons" / "melee.yaml", "melee")
    ranged = load_weapon_file(DATA_DIR / "weapons" / "ranged.yaml", "ranged")
    firearms = load_weapon_file(DATA_DIR / "weapons" / "firearms.yaml", "firearm")

    ammo_raw = load_yaml(DATA_DIR / "weapons" / "ammunition.yaml")
    ammo = [AmmoEntry(**row) for row in ammo_raw]
    check_duplicate_names([a.name for a in ammo], "ammunition.yaml")

    unarmed_raw = load_yaml(DATA_DIR / "weapons" / "unarmed.yaml")
    unarmed = [UnarmedEntry(**row) for row in unarmed_raw]
    check_duplicate_names([u.name for u in unarmed], "unarmed.yaml")

    armor_raw = load_yaml(DATA_DIR / "armor" / "armor.yaml")
    armor_blocks = {}
    for key, block_data in armor_raw.items():
        block = ArmorBlock(**block_data)
        check_duplicate_names([a.name for a in block.armors], f"armor.yaml/{key}")
        armor_blocks[key] = block

    shields_raw = load_yaml(DATA_DIR / "armor" / "shields.yaml")
    shields = [ShieldEntry(**row) for row in shields_raw]
    check_duplicate_names([s.name for s in shields], "shields.yaml")

    weapons = SimpleNamespace(
        melee=SimpleNamespace(**melee),
        ranged=SimpleNamespace(**ranged),
        firearms=SimpleNamespace(**firearms),
        ammunition=ammo,
        unarmed=unarmed,
    )
    armor = SimpleNamespace(
        armor=SimpleNamespace(**armor_blocks),
        shields=shields,
    )
    return weapons, armor


def load_spell_data():
    schools = {}
    for tradition, files in SPELL_FILES.items():
        tradition_schools = {}
        for school, expected_count in files.items():
            raw = load_yaml(DATA_DIR / "spells" / tradition / f"{school}.yaml")
            spells = [SpellEntry(**row) for row in raw]
            if len(spells) != expected_count:
                raise SystemExit(f"{school}.yaml: expected {expected_count} spells, got {len(spells)}")
            check_duplicate_names([s.name for s in spells], f"{school}.yaml")
            tradition_schools[school] = spells
        schools[tradition] = SimpleNamespace(**tradition_schools)
    return SimpleNamespace(**schools)


HARD_BREAK_LABELS = {"Benefit", "Special", "Restriction"}


def ends_in_list_item(text: str) -> bool:
    last_line = text.rstrip().rsplit("\n", 1)[-1]
    return bool(re.match(r"^\s*(-|\d+\.)\s", last_line))


def feat_body(f) -> str:
    """Render Prerequisites through Special as one block, matching source formatting:
    stacked "official" fields (Benefit/Special/Restriction) are hard-break-joined with
    no blank line, while other one-off extra labels (Note, Extra Damage Scaling, ...)
    get a blank line before them - unless the preceding field's content ends inside a
    bulleted/numbered list, in which case a blank line is required regardless of label
    to properly close the list in Markdown (verified empirically against the source)."""
    chain = [("Prerequisites", f.prerequisites if f.prerequisites is not None else "None")]
    chain.append(("Benefit", f.benefit))
    for e in f.extra:
        chain.append((e.label, e.body))
    if f.special is not None:
        chain.append(("Special", f.special))

    out = []
    for i, (label, value) in enumerate(chain):
        sep = "" if value.startswith("\n") else " "
        entry = f"**{label}:**{sep}{value}"
        if i == 0:
            out.append(entry)
        else:
            _, prev_value = chain[i - 1]
            hard_break = label in HARD_BREAK_LABELS and not ends_in_list_item(prev_value)
            out.append(("  \n" if hard_break else "\n\n") + entry)
    return "".join(out)


def load_prestige_feats() -> list[PrestigeFeatEntry]:
    raw = load_yaml(DATA_DIR / "feats" / "prestige.yaml")
    feats = [PrestigeFeatEntry(**row) for row in raw]
    if len(feats) != 8:
        raise SystemExit(f"prestige.yaml: expected 8 feats, got {len(feats)}")
    check_duplicate_names([f.name for f in feats], "prestige.yaml")
    return feats


NORMAL_FEAT_FILES = {
    "general": 16, "martial": 43, "arcane": 14, "divine": 10, "hybrid": 5, "skill": 17,
}


def load_normal_feats(name: str, expected_count: int) -> list[FeatSubcategory]:
    raw = load_yaml(DATA_DIR / "feats" / f"{name}.yaml")
    subs = [FeatSubcategory(**row) for row in raw]
    total = sum(len(s.feats) for s in subs)
    if total != expected_count:
        raise SystemExit(f"{name}.yaml: expected {expected_count} feats, got {total}")
    for s in subs:
        check_duplicate_names([f.name for f in s.feats], f"{name}.yaml/{s.name}")
    return subs


def dash(value):
    if value is None or value == "":
        return "\\-"
    return str(value)


def proplist(value):
    if not value:
        return "\\-"
    return ", ".join(value)


def signed(value):
    if value is None:
        return "\\-"
    if value > 0:
        return f"\\+{value}"
    if value < 0:
        return f"\\-{abs(value)}"
    return str(value)


def make_env() -> Environment:
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )
    env.filters["dash"] = dash
    env.filters["proplist"] = proplist
    env.filters["signed"] = signed
    env.filters["feat_body"] = feat_body
    return env


def render_all() -> dict[Path, str]:
    weapons, armor = load_data()
    spells = load_spell_data()
    env = make_env()
    rendered = {
        OUTPUT_DIR / "weapons.md": env.get_template("weapons.md.j2").render(weapons=weapons),
        OUTPUT_DIR / "armor.md": env.get_template("armor.md.j2").render(armor=armor),
    }
    for tradition, files in SPELL_FILES.items():
        for school in files:
            template = env.get_template(f"magic/{tradition}/{school}.md.j2")
            school_spells = getattr(getattr(spells, tradition), school)
            rendered[MAGIC_OUTPUT_DIR / tradition / f"{school}.md"] = template.render(spells=school_spells)

    prestige_feats = load_prestige_feats()
    rendered[FEATS_OUTPUT_DIR / "prestige_feats.md"] = env.get_template(
        "feats/prestige_feats.md.j2"
    ).render(prestige_feats=prestige_feats)

    all_subs_by_file = {}
    for name, expected_count in NORMAL_FEAT_FILES.items():
        all_subs_by_file[name] = load_normal_feats(name, expected_count)

    all_feat_names = {
        f.name for subs in all_subs_by_file.values() for s in subs for f in s.feats
    }
    for name, subs in all_subs_by_file.items():
        for s in subs:
            for f in s.feats:
                for required in f.requires_feats:
                    if required not in all_feat_names:
                        raise SystemExit(
                            f"{name}.yaml: feat '{f.name}' requires unknown feat '{required}'"
                        )

    for name, subs in all_subs_by_file.items():
        rendered[FEATS_OUTPUT_DIR / f"{name}_feats.md"] = env.get_template(
            f"feats/{name}_feats.md.j2"
        ).render(subcategories=subs)
    return rendered


def main():
    parser = argparse.ArgumentParser(description="Regenerate rulebook Markdown (equipment/magic/feats) from data/")
    parser.add_argument("--check", action="store_true", help="exit nonzero if output is stale, no write")
    parser.add_argument("--diff", action="store_true", help="print unified diff, no write")
    args = parser.parse_args()

    try:
        rendered = render_all()
    except ValidationError as e:
        print(e, file=sys.stderr)
        sys.exit(1)

    if args.check or args.diff:
        stale = False
        for path, content in rendered.items():
            current = path.read_text(encoding="utf-8") if path.exists() else ""
            if current != content:
                stale = True
                if args.diff:
                    diff = difflib.unified_diff(
                        current.splitlines(keepends=True),
                        content.splitlines(keepends=True),
                        fromfile=str(path),
                        tofile=f"{path} (generated)",
                    )
                    sys.stdout.writelines(diff)
        sys.exit(1 if stale else 0)

    for path, content in rendered.items():
        path.write_text(content, encoding="utf-8")
        print(f"wrote {path}")


if __name__ == "__main__":
    main()

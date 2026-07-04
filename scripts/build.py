import argparse
import difflib
import re
import sys
from pathlib import Path
from types import SimpleNamespace

from jinja2 import Environment, FileSystemLoader
from pydantic import ValidationError

from feat_models import FeatSubcategory, PrestigeFeatEntry
from loaders import (
    DATA_DIR,
    REPO_ROOT,
    SPELL_FILES,
    check_duplicate_names,
    load_data,
    load_spell_data,
    load_yaml,
)
from progression_models import ProgressionTable, progression_milestones

TEMPLATES_DIR = REPO_ROOT / "templates"
OUTPUT_DIR = REPO_ROOT / "core" / "equipment"
MAGIC_OUTPUT_DIR = REPO_ROOT / "core" / "magic"
FEATS_OUTPUT_DIR = REPO_ROOT / "core" / "feats"
CHARACTER_OUTPUT_DIR = REPO_ROOT / "core" / "character"

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
    check_duplicate_names([f.name for f in feats], "prestige.yaml")
    return feats


NORMAL_FEAT_FILES = ["general", "martial", "arcane", "divine", "hybrid", "skill"]


def load_normal_feats(name: str) -> list[FeatSubcategory]:
    raw = load_yaml(DATA_DIR / "feats" / f"{name}.yaml")
    subs = [FeatSubcategory(**row) for row in raw]
    for s in subs:
        check_duplicate_names([f.name for f in s.feats], f"{name}.yaml/{s.name}")
    return subs


def load_progression() -> ProgressionTable:
    raw = load_yaml(DATA_DIR / "progression.yaml")
    return ProgressionTable(**raw)


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
    for name in NORMAL_FEAT_FILES:
        all_subs_by_file[name] = load_normal_feats(name)

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

    progression = load_progression()
    rendered[CHARACTER_OUTPUT_DIR / "progression_&_rewards.md"] = env.get_template(
        "character/progression_&_rewards.md.j2"
    ).render(progression=progression, milestones=progression_milestones(progression))

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

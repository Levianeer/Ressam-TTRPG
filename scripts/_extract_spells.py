"""One-time mechanical extraction of spell data from core/magic/**/*.md into data/spells/**/*.yaml.

Not part of the ongoing build pipeline - run once during migration, then delete.
"""
import re
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent

HEADER_RE = re.compile(
    r"^\*\*(?P<name>.+?)\s*\\?-\s*Mana Cost (?P<mana_cost>\d+)\*\*\s*$",
    re.MULTILINE,
)

FIELD_LABEL = {
    "casting_time": re.compile(r"-\s*\*\*Casting Time:?\*\*:?\s*"),
    "range": re.compile(r"-\s*\*\*Range:?\*\*:?\s*"),
    "duration": re.compile(r"-\s*\*\*Duration:?\*\*:?\s*"),
    "effect": re.compile(r"-\s*\*\*Effect:?\*\*:?\s*"),
}


def literal_str_representer(dumper, data):
    if "\n" in data:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


class SpellDumper(yaml.SafeDumper):
    pass


SpellDumper.add_representer(str, literal_str_representer)


def clean_multiline(text: str) -> str:
    """Strip trailing whitespace from each line (redundant Google-Docs hard-break/blank-line
    artifacts - list items and blank lines already force the same line breaks without them)."""
    return "\n".join(line.rstrip() for line in text.split("\n"))


def parse_spells(text: str) -> list[dict]:
    headers = list(HEADER_RE.finditer(text))
    spells = []
    for i, m in enumerate(headers):
        block_start = m.end()
        block_end = headers[i + 1].start() if i + 1 < len(headers) else len(text)
        block = text[block_start:block_end]

        ct_m = FIELD_LABEL["casting_time"].search(block)
        rg_m = FIELD_LABEL["range"].search(block)
        du_m = FIELD_LABEL["duration"].search(block)
        ef_m = FIELD_LABEL["effect"].search(block)

        casting_time = block[ct_m.end():].split("\n", 1)[0].rstrip()
        range_ = block[rg_m.end():].split("\n", 1)[0].rstrip()
        duration = block[du_m.end():].split("\n", 1)[0].rstrip()
        effect = clean_multiline(block[ef_m.end():].rstrip())
        # Drop known stray trailing period on Range (Terra Sepultura, Manifest Shadow)
        if range_.endswith("ft."):
            range_ = range_[:-1]

        spells.append({
            "name": m.group("name").strip(),
            "mana_cost": int(m.group("mana_cost")),
            "casting_time": casting_time,
            "range": range_,
            "duration": duration,
            "effect": effect,
        })
    return spells


def dump_yaml(spells: list[dict], out_path: Path):
    text = yaml.dump(spells, Dumper=SpellDumper, sort_keys=False, allow_unicode=True, width=1000)
    out_path.write_text(text, encoding="utf-8")


FILES = [
    ("core/magic/arcane/aeromancy.md", "data/spells/arcane/aeromancy.yaml"),
    ("core/magic/arcane/geomancy.md", "data/spells/arcane/geomancy.yaml"),
    ("core/magic/arcane/hydromancy.md", "data/spells/arcane/hydromancy.yaml"),
    ("core/magic/arcane/pyromancy.md", "data/spells/arcane/pyromancy.yaml"),
    ("core/magic/arcane/shadowmancy.md", "data/spells/arcane/shadowmancy.yaml"),
    ("core/magic/divine/benediction.md", "data/spells/divine/benediction.yaml"),
    ("core/magic/divine/cultivation.md", "data/spells/divine/cultivation.yaml"),
    ("core/magic/divine/invocation.md", "data/spells/divine/invocation.yaml"),
    ("core/magic/divine/necration.md", "data/spells/divine/necration.yaml"),
    ("core/magic/divine/subjugation.md", "data/spells/divine/subjugation.yaml"),
]

EXPECTED_COUNTS = {
    "aeromancy": 6, "geomancy": 6, "hydromancy": 6, "pyromancy": 6, "shadowmancy": 7,
    "benediction": 6, "cultivation": 6, "invocation": 6, "necration": 6, "subjugation": 6,
}

if __name__ == "__main__":
    for src, dst in FILES:
        src_path = REPO_ROOT / src
        dst_path = REPO_ROOT / dst
        text = src_path.read_text(encoding="utf-8")
        spells = parse_spells(text)
        expected = EXPECTED_COUNTS[src_path.stem]
        if len(spells) != expected:
            raise SystemExit(f"{src}: expected {expected} spells, parsed {len(spells)}")
        dump_yaml(spells, dst_path)
        print(f"{src} -> {dst} ({len(spells)} spells)")

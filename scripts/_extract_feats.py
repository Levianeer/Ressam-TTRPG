"""One-time mechanical extraction of feat data from core/feats/*.md into data/feats/*.yaml.

Not part of the ongoing build pipeline - run once during migration, then delete.
"""
import re
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent

SUBCATEGORY_RE = re.compile(r"^## (.+)$")
FEAT_HEADING_RE = re.compile(r"^### \*\*(.+)\*\*$")
PRESTIGE_HEADING_RE = re.compile(r"^## (.+)$")
TOP_LABEL_RE = re.compile(r"^\*\*([A-Za-z][^*:\n]*?):\*\*[ \t]*", re.MULTILINE)
BLURB_RE = re.compile(r"^\*(.+)\*$")
STRAY_HEADING_RE = re.compile(r"^#+\s*$")


def literal_str_representer(dumper, data):
    if "\n" in data:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


def none_representer(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:null", "null")


class FeatDumper(yaml.SafeDumper):
    pass


FeatDumper.add_representer(str, literal_str_representer)
FeatDumper.add_representer(type(None), none_representer)


def clean_block_lines(lines: list[str]) -> list[str]:
    return [l for l in lines if l.strip() != "---" and not STRAY_HEADING_RE.match(l)]


def clean_multiline(text: str) -> str:
    """Strip trailing whitespace from each line (redundant Google-Docs hard-break/blank-line
    artifacts - list items and blank lines already force the same line breaks without them)."""
    return "\n".join(line.rstrip() for line in text.split("\n"))


def parse_fields(block_text: str) -> tuple[str, dict[str, str]]:
    matches = list(TOP_LABEL_RE.finditer(block_text))
    if not matches:
        return clean_multiline(block_text.strip()), {}
    flavor = clean_multiline(block_text[: matches[0].start()].strip())
    fields: dict[str, str] = {}
    for i, m in enumerate(matches):
        label = m.group(1).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(block_text)
        value = clean_multiline(block_text[start:end].rstrip())
        fields[label] = value
    return flavor, fields


def parse_normal_feat_file(text: str) -> list[dict]:
    lines = text.split("\n")
    markers = []
    for i, line in enumerate(lines):
        if FEAT_HEADING_RE.match(line):
            markers.append(("feat", i, FEAT_HEADING_RE.match(line).group(1)))
        elif SUBCATEGORY_RE.match(line):
            markers.append(("sub", i, SUBCATEGORY_RE.match(line).group(1)))

    subcategories: list[dict] = []
    current_sub = None
    for idx, (kind, line_no, name) in enumerate(markers):
        next_line_no = markers[idx + 1][1] if idx + 1 < len(markers) else len(lines)
        if kind == "sub":
            blurb = None
            between = [l for l in lines[line_no + 1:next_line_no] if l.strip() != ""]
            if len(between) == 1 and BLURB_RE.match(between[0]):
                blurb = BLURB_RE.match(between[0]).group(1)
            current_sub = {"name": name, "blurb": blurb, "feats": []}
            subcategories.append(current_sub)
        else:
            block_lines = clean_block_lines(lines[line_no + 1:next_line_no])
            block_text = "\n".join(block_lines)
            flavor, fields = parse_fields(block_text)

            prereq = fields.get("Prerequisites")
            if prereq is not None and prereq.strip() == "None":
                prereq = None

            extra = []
            for label, value in fields.items():
                if label in ("Prerequisites", "Benefit", "Special"):
                    continue
                extra.append({"label": label, "body": value})

            feat = {
                "name": name,
                "flavor": flavor,
                "prerequisites": prereq,
                "benefit": fields.get("Benefit", ""),
                "extra": extra,
                "special": fields.get("Special"),
            }
            assert current_sub is not None, f"feat {name!r} found before any subcategory heading"
            current_sub["feats"].append(feat)

    return subcategories


PRESTIGE_OFFICIAL_FIELDS = ("Prerequisites", "Ritual", "Effect", "Mechanical Changes")


def parse_prestige_fields(block_text: str) -> tuple[str, dict[str, str]]:
    """Like parse_fields, but any label that isn't one of the 4 official prestige
    fields (Slip, Pathing Restriction, Rune Surge, Fallen Thrall Statistics, ...) is
    folded into whichever official field most recently preceded it, verbatim heading
    included, rather than becoming its own dict entry."""
    matches = list(TOP_LABEL_RE.finditer(block_text))
    if not matches:
        return clean_multiline(block_text.strip()), {}
    flavor = clean_multiline(block_text[: matches[0].start()].strip())

    fields: dict[str, str] = {}
    current_official = None
    for i, m in enumerate(matches):
        label = m.group(1).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(block_text)
        value = block_text[start:end].rstrip()

        if label in PRESTIGE_OFFICIAL_FIELDS:
            current_official = label
            fields[label] = value
        else:
            assert current_official is not None, f"one-off label {label!r} found before any official field"
            sep = "" if value.startswith("\n") else " "
            fields[current_official] += f"\n\n**{label}:**{sep}{value}"

    return flavor, {k: clean_multiline(v) for k, v in fields.items()}


def parse_prestige_file(text: str) -> list[dict]:
    lines = text.split("\n")
    markers = []
    for i, line in enumerate(lines):
        if PRESTIGE_HEADING_RE.match(line):
            markers.append((i, PRESTIGE_HEADING_RE.match(line).group(1)))

    feats = []
    for idx, (line_no, name) in enumerate(markers):
        next_line_no = markers[idx + 1][0] if idx + 1 < len(markers) else len(lines)
        block_lines = clean_block_lines(lines[line_no + 1:next_line_no])
        block_text = "\n".join(block_lines)
        flavor, fields = parse_prestige_fields(block_text)
        flavor = flavor.strip()
        if flavor.startswith("*") and flavor.endswith("*"):
            flavor = flavor[1:-1]

        feats.append({
            "name": name,
            "flavor": flavor,
            "prerequisites": fields.get("Prerequisites", ""),
            "ritual": fields.get("Ritual", ""),
            "effect": fields.get("Effect", ""),
            "mechanical_changes": fields.get("Mechanical Changes", ""),
        })
    return feats


def find_required_feats(prerequisites: str | None, self_name: str, all_names: set[str]) -> list[str]:
    if not prerequisites:
        return []
    candidates = sorted((n for n in all_names if n != self_name), key=len, reverse=True)
    matched_spans: list[tuple[int, int]] = []
    found: list[tuple[int, str]] = []
    for name in candidates:
        for m in re.finditer(re.escape(name), prerequisites):
            start, end = m.span()
            if any(start < e and s < end for s, e in matched_spans):
                continue
            # require a word boundary on each side (avoid matching inside a longer word)
            before_ok = start == 0 or not prerequisites[start - 1].isalnum()
            after_ok = end == len(prerequisites) or not prerequisites[end].isalnum()
            if before_ok and after_ok:
                matched_spans.append((start, end))
                found.append((start, name))
    found.sort(key=lambda x: x[0])
    return [name for _, name in found]


def dump_yaml(data, out_path: Path):
    text = yaml.dump(data, Dumper=FeatDumper, sort_keys=False, allow_unicode=True, width=1000)
    out_path.write_text(text, encoding="utf-8")


NORMAL_FILES = [
    ("core/feats/general_feats.md", "data/feats/general.yaml", 16),
    ("core/feats/martial_feats.md", "data/feats/martial.yaml", 43),
    ("core/feats/arcane_feats.md", "data/feats/arcane.yaml", 14),
    ("core/feats/divine_feats.md", "data/feats/divine.yaml", 10),
    ("core/feats/hybrid_feats.md", "data/feats/hybrid.yaml", 5),
    ("core/feats/skill_feats.md", "data/feats/skill.yaml", 17),
]

if __name__ == "__main__":
    parsed = []
    all_names: set[str] = set()
    for src, dst, expected in NORMAL_FILES:
        src_path = REPO_ROOT / src
        text = src_path.read_text(encoding="utf-8")
        subs = parse_normal_feat_file(text)
        total = sum(len(s["feats"]) for s in subs)
        if total != expected:
            raise SystemExit(f"{src}: expected {expected} feats, parsed {total}")
        parsed.append((src, dst, subs))
        for s in subs:
            all_names.update(f["name"] for f in s["feats"])

    for src, dst, subs in parsed:
        for s in subs:
            for f in s["feats"]:
                required = find_required_feats(f["prerequisites"], f["name"], all_names)
                if required:
                    f["requires_feats"] = required
        dst_path = REPO_ROOT / dst
        dump_yaml(subs, dst_path)
        total = sum(len(s["feats"]) for s in subs)
        print(f"{src} -> {dst} ({total} feats across {len(subs)} subcategories)")

    src_path = REPO_ROOT / "core/feats/prestige_feats.md"
    dst_path = REPO_ROOT / "data/feats/prestige.yaml"
    text = src_path.read_text(encoding="utf-8")
    feats = parse_prestige_file(text)
    if len(feats) != 8:
        raise SystemExit(f"prestige_feats.md: expected 8 feats, parsed {len(feats)}")
    dump_yaml(feats, dst_path)
    print(f"core/feats/prestige_feats.md -> data/feats/prestige.yaml ({len(feats)} feats)")

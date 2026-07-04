from pathlib import Path
from types import SimpleNamespace

import yaml

from models import AmmoEntry, ArmorBlock, ShieldEntry, UnarmedEntry, WeaponBlock
from spell_models import SpellEntry

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"

SPELL_FILES = {
    "arcane": ["aeromancy", "geomancy", "hydromancy", "pyromancy", "shadowmancy"],
    "divine": ["benediction", "cultivation", "invocation", "necration", "subjugation"],
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
    traditions = {}
    for tradition, schools in SPELL_FILES.items():
        tradition_schools = {}
        for school in schools:
            raw = load_yaml(DATA_DIR / "spells" / tradition / f"{school}.yaml")
            spells = [SpellEntry(**row) for row in raw]
            check_duplicate_names([s.name for s in spells], f"{school}.yaml")
            tradition_schools[school] = spells
        traditions[tradition] = SimpleNamespace(**tradition_schools)
    return SimpleNamespace(**traditions)

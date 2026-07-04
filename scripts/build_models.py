from dataclasses import dataclass
from typing import Literal, Optional

from pydantic import BaseModel, Field

Attribute = Literal["STR", "REF", "END", "DEX", "MIND", "ARC", "FAI", "CHA"]


class EquipmentLoadout(BaseModel):
    weapon: str
    weapon_attribute: Attribute
    armor: Optional[str] = None
    shield: Optional[str] = None


class AttributeBlock(BaseModel):
    STR: int = Field(ge=1, le=10)
    REF: int = Field(ge=1, le=10)
    END: int = Field(ge=1, le=10)
    DEX: int = Field(ge=1, le=10)
    MIND: int = Field(ge=1, le=10)
    ARC: int = Field(ge=1, le=10)
    FAI: int = Field(ge=1, le=10)
    CHA: int = Field(ge=1, le=10)


class LevelDelta(BaseModel):
    level: int = Field(ge=2, le=12)
    attribute_changes: dict[Attribute, int] = Field(default_factory=dict)
    skill_changes: dict[str, int] = Field(default_factory=dict)
    equipment: Optional[EquipmentLoadout] = None


class Archetype(BaseModel):
    key: str
    name: str
    description: str
    weapon_skill: str
    school_skill: Optional[str] = None
    starting_attributes: AttributeBlock
    starting_skills: dict[str, int] = Field(default_factory=dict)
    starting_equipment: EquipmentLoadout
    level_deltas: list[LevelDelta] = Field(default_factory=list)

    def snapshot(self, level: int) -> "CharacterSnapshot":
        """Resolves cumulative attributes/skills/equipment as of `level` by
        folding starting state with every level_delta up to and including it."""
        attributes = self.starting_attributes.model_dump()
        skills = dict(self.starting_skills)
        equipment = self.starting_equipment
        for delta in sorted(self.level_deltas, key=lambda d: d.level):
            if delta.level > level:
                break
            for attr, change in delta.attribute_changes.items():
                attributes[attr] = attributes.get(attr, 0) + change
            for skill, change in delta.skill_changes.items():
                skills[skill] = skills.get(skill, 0) + change
            if delta.equipment is not None:
                equipment = delta.equipment
        return CharacterSnapshot(level=level, attributes=attributes, skills=skills, equipment=equipment)


@dataclass
class CharacterSnapshot:
    level: int
    attributes: dict[str, int]
    skills: dict[str, int]
    equipment: EquipmentLoadout

    @property
    def armorer_ranks(self) -> int:
        """Armorer is itself a skill (Defense & Survival category, core_rules.md:117),
        not a separate tracked stat - reduces effective_armor_penalty() in formulas.py."""
        return self.skills.get("Armorer", 0)

    @property
    def agility_skill(self) -> int:
        """Agility is itself a skill (Adroitness & Subterfuge category, core_rules.md:118),
        used as the 'agility_skill' input to formulas.evasion()."""
        return self.skills.get("Agility", 0)


def check_archetype_budget(archetype: Archetype, progression) -> list[str]:
    """Soft cross-check (returns warnings, never raises): flags if an archetype
    spends more attribute/skill points than data/progression.yaml grants by a
    given level. Kept as warnings rather than validation errors since an
    archetype might intentionally under-spend for contrast with an optimized build."""
    warnings = []
    starting_attr_spend = sum(archetype.starting_attributes.model_dump().values())
    starting_skill_spend = sum(archetype.starting_skills.values())
    if starting_attr_spend > progression.character_creation.starting_attribute_points:
        warnings.append(
            f"{archetype.key}: starting attributes spend {starting_attr_spend} > "
            f"budget {progression.character_creation.starting_attribute_points}"
        )
    if starting_skill_spend > progression.character_creation.starting_skill_points:
        warnings.append(
            f"{archetype.key}: starting skills spend {starting_skill_spend} > "
            f"budget {progression.character_creation.starting_skill_points}"
        )
    for delta in archetype.level_deltas:
        lvl = progression.level(delta.level)
        attr_spend = sum(delta.attribute_changes.values())
        skill_spend = sum(delta.skill_changes.values())
        if attr_spend > lvl.attribute_points_gained:
            warnings.append(
                f"{archetype.key}: level {delta.level} spends {attr_spend} attribute "
                f"points but only {lvl.attribute_points_gained} were gained"
            )
        if skill_spend > lvl.skill_points_gained:
            warnings.append(
                f"{archetype.key}: level {delta.level} spends {skill_spend} skill "
                f"points but only {lvl.skill_points_gained} were gained"
            )
    return warnings

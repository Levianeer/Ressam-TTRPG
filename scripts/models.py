from typing import Literal, Optional

from pydantic import BaseModel, Field, model_validator


class WeaponEntry(BaseModel):
    name: str
    damage: str
    properties: list[str] = Field(default_factory=list)
    critical: Optional[str] = None
    cost: str
    weight: str
    range: Optional[str] = None


class WeaponBlock(BaseModel):
    category: str
    skill: str
    kind: Literal["melee", "ranged", "firearm"]
    weapons: list[WeaponEntry]

    @model_validator(mode="after")
    def check_range_matches_kind(self):
        needs_range = self.kind in ("ranged", "firearm")
        for weapon in self.weapons:
            if needs_range and weapon.range is None:
                raise ValueError(
                    f"{self.category}/{weapon.name}: missing 'range' for a {self.kind} weapon"
                )
            if not needs_range and weapon.range is not None:
                raise ValueError(
                    f"{self.category}/{weapon.name}: 'range' set on a melee weapon"
                )
        return self


class AmmoEntry(BaseModel):
    name: str
    cost: str
    weight: str


class UnarmedEntry(BaseModel):
    name: str
    damage: str
    properties: list[str] = Field(default_factory=list)
    critical: Optional[str] = None


class ArmorEntry(BaseModel):
    name: str
    ar: Optional[int] = None
    penalty: Optional[int] = None
    stealth: Optional[int] = None
    price: str
    weight: str


class ArmorBlock(BaseModel):
    category: str
    armors: list[ArmorEntry]


class ShieldEntry(BaseModel):
    name: str
    ar_bonus: Optional[int] = None
    penalty: Optional[int] = None
    properties: list[str] = Field(default_factory=list)
    price: str
    weight: str

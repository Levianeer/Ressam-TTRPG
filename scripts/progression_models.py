from types import SimpleNamespace
from typing import Optional

from pydantic import BaseModel, Field, model_validator


class ProgressionLevel(BaseModel):
    level: int = Field(ge=1, le=12)
    total_xp: int
    skill_points_gained: int = Field(ge=0)
    skill_cap: int
    attribute_points_gained: int = Field(ge=0)
    attribute_cap: int
    feats_gained: int = Field(ge=0)
    notes: Optional[str] = None


class CharacterCreationPool(BaseModel):
    starting_skill_points: int
    starting_attribute_points: int
    starting_feats: int


class ProgressionTable(BaseModel):
    xp_per_level: int
    character_creation: CharacterCreationPool
    levels: list[ProgressionLevel]

    @model_validator(mode="after")
    def check_consistency(self):
        for position, lvl in enumerate(self.levels, start=1):
            if lvl.level != position:
                raise ValueError(
                    f"progression.yaml: levels must be contiguous starting at 1, "
                    f"found level {lvl.level} at position {position}"
                )
            expected_xp = self.xp_per_level * lvl.level**2
            if lvl.total_xp != expected_xp:
                raise ValueError(
                    f"progression.yaml: level {lvl.level} total_xp={lvl.total_xp} "
                    f"does not match xp_per_level * level^2={expected_xp}"
                )
        for prev, curr in zip(self.levels, self.levels[1:]):
            if curr.skill_cap < prev.skill_cap:
                raise ValueError(
                    f"progression.yaml: skill_cap regresses from level {prev.level} "
                    f"({prev.skill_cap}) to level {curr.level} ({curr.skill_cap})"
                )
            if curr.attribute_cap < prev.attribute_cap:
                raise ValueError(
                    f"progression.yaml: attribute_cap regresses from level {prev.level} "
                    f"({prev.attribute_cap}) to level {curr.level} ({curr.attribute_cap})"
                )
        return self

    def level(self, n: int) -> ProgressionLevel:
        return self.levels[n - 1]

    def cumulative_skill_points(self, n: int) -> int:
        """Total skill points a character has to spend by the end of level n."""
        return self.character_creation.starting_skill_points + sum(
            lvl.skill_points_gained for lvl in self.levels[:n]
        )

    def cumulative_attribute_points(self, n: int) -> int:
        """Total attribute points a character has to spend by the end of level n."""
        return self.character_creation.starting_attribute_points + sum(
            lvl.attribute_points_gained for lvl in self.levels[:n]
        )


def progression_milestones(table: ProgressionTable) -> SimpleNamespace:
    """Derives the 'cap reached at level N' facts from the level data itself,
    so the Per Level Advancement bullets don't hardcode them separately."""
    max_skill_cap = max(lvl.skill_cap for lvl in table.levels)
    max_attribute_cap = max(lvl.attribute_cap for lvl in table.levels)
    return SimpleNamespace(
        max_skill_cap=max_skill_cap,
        max_attribute_cap=max_attribute_cap,
        skill_cap_reached_at=next(
            lvl.level for lvl in table.levels if lvl.skill_cap == max_skill_cap
        ),
        attribute_cap_reached_at=next(
            lvl.level for lvl in table.levels if lvl.attribute_cap == max_attribute_cap
        ),
        max_total_xp=table.levels[-1].total_xp,
    )

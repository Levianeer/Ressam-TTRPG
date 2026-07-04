from pydantic import BaseModel, Field


class SpellEntry(BaseModel):
    name: str
    mana_cost: int = Field(ge=1, le=5)
    casting_time: str
    range: str
    duration: str
    effect: str

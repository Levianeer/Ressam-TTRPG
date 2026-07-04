from typing import Optional

from pydantic import BaseModel, Field


class FeatExtraField(BaseModel):
    label: str
    body: str


class FeatEntry(BaseModel):
    name: str
    flavor: str
    prerequisites: Optional[str] = None
    benefit: str
    extra: list[FeatExtraField] = Field(default_factory=list)
    special: Optional[str] = None
    requires_feats: list[str] = Field(default_factory=list)


class FeatSubcategory(BaseModel):
    name: str
    blurb: Optional[str] = None
    feats: list[FeatEntry]


class PrestigeFeatEntry(BaseModel):
    name: str
    flavor: str
    prerequisites: str
    ritual: str
    effect: str
    mechanical_changes: str

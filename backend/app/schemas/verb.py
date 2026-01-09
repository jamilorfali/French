"""
Verb schemas for API validation.
"""
from pydantic import BaseModel
from typing import Optional


class ConjugationResponse(BaseModel):
    """Schema for verb conjugation response."""
    tense: str
    mood: str
    je: Optional[str] = None
    tu: Optional[str] = None
    il_elle: Optional[str] = None
    nous: Optional[str] = None
    vous: Optional[str] = None
    ils_elles: Optional[str] = None
    spanish_equivalent: Optional[str] = None

    class Config:
        from_attributes = True


class VerbResponse(BaseModel):
    """Schema for verb list response."""
    id: int
    infinitive: str
    english: str
    spanish: Optional[str] = None
    group: int
    is_irregular: bool
    cefr_level_id: int

    class Config:
        from_attributes = True


class VerbDetail(VerbResponse):
    """Schema for detailed verb response."""
    auxiliary: str
    past_participle: Optional[str] = None
    present_participle: Optional[str] = None
    notes: Optional[str] = None
    is_reflexive: bool = False
    spanish_comparison: Optional[str] = None
    conjugations: list[ConjugationResponse] = []

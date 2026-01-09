"""
Vocabulary schemas for API validation.
"""
from pydantic import BaseModel
from typing import Optional


class VocabularyResponse(BaseModel):
    """Schema for vocabulary list response."""
    id: int
    french: str
    english: str
    spanish: Optional[str] = None
    gender: Optional[str] = None
    part_of_speech: str
    category: Optional[str] = None
    is_cognate: bool = False

    class Config:
        from_attributes = True


class VocabularyDetail(VocabularyResponse):
    """Schema for detailed vocabulary response."""
    cefr_level_id: int
    plural: Optional[str] = None
    phonetic: Optional[str] = None
    cognate_spanish: Optional[str] = None
    cognate_note: Optional[str] = None
    is_false_friend: bool = False
    example_french: Optional[str] = None
    example_english: Optional[str] = None
    example_spanish: Optional[str] = None
    notes: Optional[str] = None

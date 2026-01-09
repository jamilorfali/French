"""
Grammar schemas for API validation.
"""
from pydantic import BaseModel
from typing import Optional, Any


class GrammarResponse(BaseModel):
    """Schema for grammar list response."""
    id: int
    topic: str
    title: str
    cefr_level_id: int
    order: int

    class Config:
        from_attributes = True


class GrammarDetail(GrammarResponse):
    """Schema for detailed grammar response."""
    explanation_en: str
    explanation_es: Optional[str] = None
    spanish_comparison: Optional[str] = None
    examples: list[dict[str, Any]] = []
    common_mistakes: list[str] = []
    tips: list[str] = []
    related_topics: list[str] = []

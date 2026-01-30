"""
Lesson schemas for API validation.
"""
from pydantic import BaseModel
from typing import Optional


class LessonResponse(BaseModel):
    """Schema for lesson list response."""
    id: int
    cefr_level_id: int
    unit_number: int
    title: str
    description: Optional[str] = None
    estimated_duration: int
    objectives: list[str] = []
    themes: list[str] = []

    class Config:
        from_attributes = True


class LessonDetail(LessonResponse):
    """Schema for detailed lesson response."""
    grammar_topics: list[str] = []

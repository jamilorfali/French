"""
Exercise schemas for API validation.
"""
from pydantic import BaseModel
from typing import Optional, Any


class ExerciseContent(BaseModel):
    """Schema for exercise content."""
    type: str
    data: dict[str, Any]


class ExerciseResponse(BaseModel):
    """Schema for exercise response."""
    id: int
    exercise_type: str
    difficulty: str
    content: dict[str, Any]
    hints: list[str] = []
    spanish_hint: Optional[str] = None
    tags: list[str] = []

    # Note: answer is intentionally excluded to prevent cheating
    # It's only revealed after submitting an answer

    class Config:
        from_attributes = True


class ExerciseWithAnswer(ExerciseResponse):
    """Schema for exercise with answer (for review/results)."""
    answer: dict[str, Any]
    explanation: Optional[str] = None

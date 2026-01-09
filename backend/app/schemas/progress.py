"""
Progress and practice session schemas for API validation.
"""
from pydantic import BaseModel
from typing import Optional, Any
from datetime import datetime


class ProgressResponse(BaseModel):
    """Schema for user progress on an item."""
    id: int
    item_type: str
    item_id: int
    ease_factor: float
    interval: int
    repetitions: int
    next_review: Optional[datetime] = None
    last_reviewed: Optional[datetime] = None
    correct_count: int
    incorrect_count: int
    accuracy: float

    class Config:
        from_attributes = True


class PracticeSessionCreate(BaseModel):
    """Schema for starting a practice session."""
    session_type: str = "mixed"  # mixed, vocabulary, conjugation, listening, speaking, gender
    duration_mins: int = 15  # 5, 15, or 30
    focus_areas: list[str] = []  # specific areas to focus on
    cefr_level: Optional[str] = None  # specific level, or None for current


class PracticeSessionResponse(BaseModel):
    """Schema for practice session response."""
    id: int
    session_type: str
    target_duration_mins: int
    actual_duration_mins: Optional[int] = None
    items_practiced: int
    correct_count: int
    incorrect_count: int
    accuracy: float
    started_at: datetime
    completed_at: Optional[datetime] = None
    focus_areas: list[str] = []
    exercise_types: list[str] = []

    class Config:
        from_attributes = True


class AnswerSubmit(BaseModel):
    """Schema for submitting an answer."""
    exercise_id: int
    answer: Any  # Structure varies by exercise type
    time_taken_seconds: int = 0


class AnswerResult(BaseModel):
    """Schema for answer result."""
    correct: bool
    correct_answer: Any
    explanation: Optional[str] = None
    spanish_note: Optional[str] = None
    points_earned: int = 0
    streak: int = 0


class OverallProgress(BaseModel):
    """Schema for overall progress summary."""
    current_level: str
    vocabulary_learned: int
    vocabulary_total: int
    grammar_learned: int
    grammar_total: int
    verbs_learned: int
    verbs_total: int
    total_practice_time_mins: int
    current_streak_days: int
    accuracy_7_days: float
    items_due_for_review: int


class WeakArea(BaseModel):
    """Schema for a weak area needing attention."""
    area_type: str  # vocabulary, grammar, verb, exercise_type
    area_name: str
    accuracy: float
    last_practiced: Optional[datetime] = None
    recommended_exercises: int

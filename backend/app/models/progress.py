"""
Progress tracking models - user progress and practice sessions.
"""
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, JSON, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from ..database import Base


class ItemType(str, enum.Enum):
    """Types of items that can be tracked for progress."""
    VOCABULARY = "vocabulary"
    GRAMMAR = "grammar"
    VERB = "verb"
    EXERCISE = "exercise"


class UserProgress(Base):
    """
    Tracks user progress on individual items using spaced repetition.
    Based on SM-2 algorithm.
    """

    __tablename__ = "user_progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # What item is being tracked
    item_type = Column(Enum(ItemType), nullable=False, index=True)
    item_id = Column(Integer, nullable=False, index=True)

    # SM-2 Algorithm fields
    ease_factor = Column(Float, default=2.5)  # Starts at 2.5
    interval = Column(Integer, default=1)  # Days until next review
    repetitions = Column(Integer, default=0)  # Successful reviews in a row

    # Scheduling
    next_review = Column(DateTime(timezone=True), index=True)
    last_reviewed = Column(DateTime(timezone=True))

    # Statistics
    correct_count = Column(Integer, default=0)
    incorrect_count = Column(Integer, default=0)
    total_time_seconds = Column(Integer, default=0)  # Time spent on this item

    # Last quality rating (0-5)
    last_quality = Column(Integer)

    def __repr__(self):
        return f"<UserProgress {self.item_type.value}:{self.item_id}>"

    @property
    def accuracy(self) -> float:
        """Calculate accuracy percentage."""
        total = self.correct_count + self.incorrect_count
        if total == 0:
            return 0.0
        return (self.correct_count / total) * 100


class PracticeSession(Base):
    """Records a practice session."""

    __tablename__ = "practice_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Session type
    session_type = Column(String(50), default="mixed")  # mixed, vocabulary, conjugation, listening, etc.

    # Duration
    target_duration_mins = Column(Integer, default=15)  # Requested duration
    actual_duration_mins = Column(Integer)  # Actual time spent

    # Items practiced
    items_practiced = Column(Integer, default=0)
    correct_count = Column(Integer, default=0)
    incorrect_count = Column(Integer, default=0)

    # Focus areas for this session
    focus_areas = Column(JSON, default=list)

    # Exercise types used
    exercise_types = Column(JSON, default=list)

    # Timing
    started_at = Column(DateTime(timezone=True), server_default=func.now())
    completed_at = Column(DateTime(timezone=True))

    # Session data (exercises completed, responses, etc.)
    session_data = Column(JSON, default=dict)

    def __repr__(self):
        return f"<PracticeSession {self.id} - {self.session_type}>"

    @property
    def accuracy(self) -> float:
        """Calculate session accuracy percentage."""
        total = self.correct_count + self.incorrect_count
        if total == 0:
            return 0.0
        return (self.correct_count / total) * 100

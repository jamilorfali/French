"""
Exercise model - various exercise types for practice.
"""
from sqlalchemy import Column, Integer, String, Text, ForeignKey, JSON, Enum
from sqlalchemy.orm import relationship
import enum
from ..database import Base


class ExerciseType(str, enum.Enum):
    """Types of exercises available."""
    VOCABULARY_FLASHCARD = "vocabulary_flashcard"
    MULTIPLE_CHOICE = "multiple_choice"
    LISTENING = "listening"
    SPEAKING = "speaking"
    CONJUGATION = "conjugation"
    GENDER = "gender"
    SENTENCE_BUILDER = "sentence_builder"
    FILL_BLANK = "fill_blank"
    TRANSLATION = "translation"
    READING = "reading"
    MATCHING = "matching"


class Difficulty(str, enum.Enum):
    """Exercise difficulty levels."""
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class Exercise(Base):
    """An exercise/activity for practice."""

    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)
    lesson_id = Column(Integer, ForeignKey("lessons.id"), nullable=True)

    # Exercise classification
    exercise_type = Column(Enum(ExerciseType), nullable=False, index=True)
    difficulty = Column(Enum(Difficulty), default=Difficulty.MEDIUM)

    # Exercise content (structure varies by type - see ARCHITECTURE.md)
    content = Column(JSON, nullable=False)

    # Correct answer(s) - structure varies by type
    answer = Column(JSON, nullable=False)

    # Hints to show on request
    hints = Column(JSON, default=list)

    # Spanish hint (leveraging Spanish knowledge)
    spanish_hint = Column(Text)

    # Explanation shown after answering
    explanation = Column(Text)

    # Tags for filtering (e.g., ["verbs", "present_tense", "être"])
    tags = Column(JSON, default=list)

    # Related vocabulary/grammar IDs
    vocabulary_ids = Column(JSON, default=list)
    grammar_ids = Column(JSON, default=list)
    verb_ids = Column(JSON, default=list)

    # Relationships
    lesson = relationship("Lesson", back_populates="exercises")

    def __repr__(self):
        return f"<Exercise {self.exercise_type.value} - {self.difficulty.value}>"

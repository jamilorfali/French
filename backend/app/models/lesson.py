"""
Lesson model - organized units of learning content.
"""
from sqlalchemy import Column, Integer, String, Text, ForeignKey, JSON
from sqlalchemy.orm import relationship
from ..database import Base


class Lesson(Base):
    """A lesson/unit within a CEFR level."""

    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    cefr_level_id = Column(Integer, ForeignKey("cefr_levels.id"), nullable=False)

    # Lesson structure
    unit_number = Column(Integer, nullable=False)  # Unit 1, 2, 3...
    title = Column(String(200), nullable=False)
    description = Column(Text)

    # Learning objectives (list of strings)
    objectives = Column(JSON, default=list)

    # Themes covered (e.g., "greetings", "family", "food")
    themes = Column(JSON, default=list)

    # Grammar topics in this lesson
    grammar_topics = Column(JSON, default=list)

    # Estimated time to complete (minutes)
    estimated_duration = Column(Integer, default=30)

    # Relationships
    cefr_level = relationship("CEFRLevel", back_populates="lessons")
    exercises = relationship("Exercise", back_populates="lesson")

    def __repr__(self):
        return f"<Lesson {self.unit_number}: {self.title}>"

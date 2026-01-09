"""
CEFR Level model - A1 through C2.
"""
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from ..database import Base


class CEFRLevel(Base):
    """CEFR language proficiency levels."""

    __tablename__ = "cefr_levels"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(2), unique=True, nullable=False, index=True)  # A1, A2, B1, B2, C1, C2
    name = Column(String(50), nullable=False)  # "Beginner", "Elementary", etc.
    description = Column(Text)
    order = Column(Integer, nullable=False)  # 1-6 for sorting

    # Alliance Française mapping
    af_levels = Column(String(50))  # e.g., "A100-A105"

    # Expected vocabulary count at this level
    vocabulary_target = Column(Integer, default=500)

    # Relationships
    lessons = relationship("Lesson", back_populates="cefr_level")
    vocabulary = relationship("Vocabulary", back_populates="cefr_level")
    grammar = relationship("Grammar", back_populates="cefr_level")
    verbs = relationship("Verb", back_populates="cefr_level")

    def __repr__(self):
        return f"<CEFRLevel {self.code}: {self.name}>"

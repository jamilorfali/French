"""
Grammar model - French grammar rules and explanations.
"""
from sqlalchemy import Column, Integer, String, Text, ForeignKey, JSON
from sqlalchemy.orm import relationship
from ..database import Base


class Grammar(Base):
    """French grammar topic with explanations in English and Spanish."""

    __tablename__ = "grammar"

    id = Column(Integer, primary_key=True, index=True)
    cefr_level_id = Column(Integer, ForeignKey("cefr_levels.id"), nullable=False)

    # Topic identification
    topic = Column(String(100), nullable=False, index=True)  # e.g., "present_tense", "articles"
    title = Column(String(200), nullable=False)  # Display title

    # Explanations
    explanation_en = Column(Text, nullable=False)  # English explanation
    explanation_es = Column(Text)  # Spanish explanation

    # Spanish comparison (leverage existing knowledge)
    spanish_comparison = Column(Text)  # How this differs from Spanish grammar

    # Examples (list of {french, english, spanish})
    examples = Column(JSON, default=list)

    # Common mistakes to avoid
    common_mistakes = Column(JSON, default=list)

    # Tips and memory aids
    tips = Column(JSON, default=list)

    # Related grammar topics
    related_topics = Column(JSON, default=list)

    # Order within level for sequential learning
    order = Column(Integer, default=0)

    # Relationships
    cefr_level = relationship("CEFRLevel", back_populates="grammar")

    def __repr__(self):
        return f"<Grammar {self.topic}: {self.title}>"

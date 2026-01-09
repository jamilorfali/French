"""
Verb models - French verbs and their conjugations.
"""
from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum
from ..database import Base


class VerbGroup(int, enum.Enum):
    """French verb conjugation groups."""
    FIRST = 1   # -er verbs (parler)
    SECOND = 2  # -ir verbs (finir)
    THIRD = 3   # Irregular verbs (-re, -oir, etc.)


class Auxiliary(str, enum.Enum):
    """Auxiliary verb used in compound tenses."""
    AVOIR = "avoir"
    ETRE = "être"


class Verb(Base):
    """French verb with basic information."""

    __tablename__ = "verbs"

    id = Column(Integer, primary_key=True, index=True)
    cefr_level_id = Column(Integer, ForeignKey("cefr_levels.id"), nullable=False)

    # Infinitive form
    infinitive = Column(String(100), nullable=False, unique=True, index=True)

    # Translations
    english = Column(String(200), nullable=False)
    spanish = Column(String(200))  # Spanish equivalent

    # Conjugation group
    group = Column(Enum(VerbGroup), nullable=False)

    # Is it irregular within its group?
    is_irregular = Column(Boolean, default=False)

    # Auxiliary for compound tenses
    auxiliary = Column(Enum(Auxiliary), default=Auxiliary.AVOIR)

    # Past participle (for compound tenses)
    past_participle = Column(String(100))

    # Present participle
    present_participle = Column(String(100))

    # Usage notes
    notes = Column(Text)

    # Is it reflexive? (se + verb)
    is_reflexive = Column(Boolean, default=False)

    # Spanish comparison notes
    spanish_comparison = Column(Text)

    # Relationships
    cefr_level = relationship("CEFRLevel", back_populates="verbs")
    conjugations = relationship("VerbConjugation", back_populates="verb", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Verb {self.infinitive}>"


class VerbConjugation(Base):
    """Conjugation of a verb in a specific tense/mood."""

    __tablename__ = "verb_conjugations"

    id = Column(Integer, primary_key=True, index=True)
    verb_id = Column(Integer, ForeignKey("verbs.id"), nullable=False)

    # Tense and mood
    tense = Column(String(50), nullable=False, index=True)  # present, imparfait, passé_composé, etc.
    mood = Column(String(50), nullable=False, default="indicatif")  # indicatif, subjonctif, conditionnel, impératif

    # Conjugated forms
    je = Column(String(100))
    tu = Column(String(100))
    il_elle = Column(String(100))
    nous = Column(String(100))
    vous = Column(String(100))
    ils_elles = Column(String(100))

    # Spanish equivalent conjugation (for comparison)
    spanish_equivalent = Column(String(200))

    # Relationships
    verb = relationship("Verb", back_populates="conjugations")

    def __repr__(self):
        return f"<VerbConjugation {self.verb.infinitive} - {self.tense}>"

"""
Vocabulary model - French words with translations and metadata.
"""
from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum
from ..database import Base


class PartOfSpeech(str, enum.Enum):
    """Parts of speech for vocabulary items."""
    NOUN = "noun"
    VERB = "verb"
    ADJECTIVE = "adjective"
    ADVERB = "adverb"
    PRONOUN = "pronoun"
    PREPOSITION = "preposition"
    CONJUNCTION = "conjunction"
    INTERJECTION = "interjection"
    ARTICLE = "article"
    DETERMINER = "determiner"
    PHRASE = "phrase"


class Gender(str, enum.Enum):
    """Grammatical gender for French nouns."""
    MASCULINE = "m"
    FEMININE = "f"
    BOTH = "mf"  # Some nouns can be both
    NONE = "-"  # For non-gendered words (verbs, adverbs, etc.)


class Vocabulary(Base):
    """French vocabulary item with translations."""

    __tablename__ = "vocabulary"

    id = Column(Integer, primary_key=True, index=True)
    cefr_level_id = Column(Integer, ForeignKey("cefr_levels.id"), nullable=False)

    # The French word/phrase
    french = Column(String(200), nullable=False, index=True)

    # Translations
    english = Column(String(200), nullable=False)
    spanish = Column(String(200))  # Spanish translation for cognate comparison

    # Grammatical info
    gender = Column(Enum(Gender), default=Gender.NONE)
    part_of_speech = Column(Enum(PartOfSpeech), nullable=False)
    plural = Column(String(200))  # Plural form if irregular

    # Pronunciation
    phonetic = Column(String(200))  # IPA transcription

    # Cognate information (Spanish-French connection)
    is_cognate = Column(Boolean, default=False)
    cognate_spanish = Column(String(200))  # The similar Spanish word
    cognate_note = Column(Text)  # Explanation of similarity/difference
    is_false_friend = Column(Boolean, default=False)  # Words that look similar but differ

    # Category for grouping (e.g., "food", "family", "colors")
    category = Column(String(100), index=True)

    # Example sentences
    example_french = Column(Text)
    example_english = Column(Text)
    example_spanish = Column(Text)

    # Notes for learner
    notes = Column(Text)

    # Relationships
    cefr_level = relationship("CEFRLevel", back_populates="vocabulary")

    def __repr__(self):
        return f"<Vocabulary {self.french} ({self.english})>"

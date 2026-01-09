"""
User model for storing learner profile and settings.
"""
from sqlalchemy import Column, Integer, String, DateTime, JSON
from sqlalchemy.sql import func
from ..database import Base


class User(Base):
    """User profile and settings."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)

    # Language background
    native_language = Column(String(10), default="en-US")  # BCP-47 code
    secondary_language = Column(String(10), default="es-ES")  # Spanish (Spain)
    target_language = Column(String(10), default="fr-FR")  # French

    # Current progress
    current_cefr_level = Column(String(2), default="A1")

    # Settings (JSON for flexibility)
    settings = Column(JSON, default=lambda: {
        "session_duration": 15,
        "speech_rate": 0.9,
        "show_spanish_hints": True,
        "show_phonetic": True,
        "daily_goal": 20,  # exercises per day
        "focus_areas": ["listening", "conjugation", "gender", "pronunciation"]
    })

    # Metadata
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    last_active = Column(DateTime(timezone=True))

    def __repr__(self):
        return f"<User {self.name} - {self.current_cefr_level}>"

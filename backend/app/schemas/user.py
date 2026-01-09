"""
User schemas for API validation.
"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserSettings(BaseModel):
    """User settings schema."""
    session_duration: int = 15
    speech_rate: float = 0.9
    show_spanish_hints: bool = True
    show_phonetic: bool = True
    daily_goal: int = 20
    focus_areas: list[str] = ["listening", "conjugation", "gender", "pronunciation"]


class UserBase(BaseModel):
    """Base user schema."""
    name: str
    native_language: str = "en-US"
    secondary_language: str = "es-ES"
    target_language: str = "fr-FR"
    current_cefr_level: str = "A1"


class UserCreate(UserBase):
    """Schema for creating a user."""
    settings: Optional[UserSettings] = None


class UserUpdate(BaseModel):
    """Schema for updating a user."""
    name: Optional[str] = None
    current_cefr_level: Optional[str] = None
    settings: Optional[UserSettings] = None


class UserResponse(UserBase):
    """Schema for user response."""
    id: int
    settings: dict
    created_at: datetime
    updated_at: Optional[datetime] = None
    last_active: Optional[datetime] = None

    class Config:
        from_attributes = True

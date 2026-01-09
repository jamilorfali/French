"""
User profile API endpoints.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from ..database import get_db
from ..models import User
from ..schemas import UserResponse, UserUpdate

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/profile", response_model=UserResponse)
def get_user_profile(db: Session = Depends(get_db)):
    """Get the current user's profile."""
    user = db.query(User).first()

    if not user:
        # Create default user for first-time access
        user = User(
            name="French Learner",
            native_language="en-US",
            secondary_language="es-ES",
            target_language="fr-FR",
            current_cefr_level="A1",
            settings={
                "session_duration": 15,
                "speech_rate": 0.9,
                "show_spanish_hints": True,
                "show_phonetic": True,
                "daily_goal": 20,
                "focus_areas": ["listening", "conjugation", "gender", "pronunciation"]
            }
        )
        db.add(user)
        db.commit()
        db.refresh(user)

    return user


@router.put("/profile", response_model=UserResponse)
def update_user_profile(
    updates: UserUpdate,
    db: Session = Depends(get_db)
):
    """Update user profile."""
    user = db.query(User).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if updates.name is not None:
        user.name = updates.name

    if updates.current_cefr_level is not None:
        valid_levels = ["A1", "A2", "B1", "B2", "C1", "C2"]
        if updates.current_cefr_level.upper() not in valid_levels:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid CEFR level. Must be one of: {valid_levels}"
            )
        user.current_cefr_level = updates.current_cefr_level.upper()

    if updates.settings is not None:
        # Merge with existing settings
        current_settings = user.settings or {}
        current_settings.update(updates.settings.model_dump(exclude_none=True))
        user.settings = current_settings

    user.updated_at = datetime.now()
    db.commit()
    db.refresh(user)

    return user


@router.post("/touch")
def touch_user_activity(db: Session = Depends(get_db)):
    """Update user's last active timestamp."""
    user = db.query(User).first()
    if user:
        user.last_active = datetime.now()
        db.commit()
    return {"status": "ok"}

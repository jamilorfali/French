"""
CEFR Levels API endpoints.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models import CEFRLevel
from ..schemas import CEFRLevelResponse

router = APIRouter(prefix="/levels", tags=["levels"])


@router.get("/", response_model=List[CEFRLevelResponse])
def get_all_levels(db: Session = Depends(get_db)):
    """Get all CEFR levels."""
    levels = db.query(CEFRLevel).order_by(CEFRLevel.order).all()
    return levels


@router.get("/{level_code}", response_model=CEFRLevelResponse)
def get_level(level_code: str, db: Session = Depends(get_db)):
    """Get a specific CEFR level by code (A1, A2, etc.)."""
    level = db.query(CEFRLevel).filter(CEFRLevel.code == level_code.upper()).first()
    if not level:
        raise HTTPException(status_code=404, detail=f"Level {level_code} not found")
    return level

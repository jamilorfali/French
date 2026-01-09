"""
Lessons API endpoints.
"""
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from ..database import get_db
from ..models import Lesson, CEFRLevel
from ..schemas import LessonResponse, LessonDetail

router = APIRouter(prefix="/lessons", tags=["lessons"])


@router.get("/", response_model=List[LessonResponse])
def get_lessons(
    level: Optional[str] = Query(None, description="Filter by CEFR level (A1, A2, etc.)"),
    db: Session = Depends(get_db)
):
    """Get all lessons, optionally filtered by CEFR level."""
    query = db.query(Lesson)

    if level:
        cefr_level = db.query(CEFRLevel).filter(CEFRLevel.code == level.upper()).first()
        if cefr_level:
            query = query.filter(Lesson.cefr_level_id == cefr_level.id)

    lessons = query.order_by(Lesson.cefr_level_id, Lesson.unit_number).all()
    return lessons


@router.get("/{lesson_id}", response_model=LessonDetail)
def get_lesson(lesson_id: int, db: Session = Depends(get_db)):
    """Get a specific lesson by ID."""
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return lesson


@router.get("/level/{level_code}", response_model=List[LessonResponse])
def get_lessons_by_level(level_code: str, db: Session = Depends(get_db)):
    """Get all lessons for a specific CEFR level."""
    level = db.query(CEFRLevel).filter(CEFRLevel.code == level_code.upper()).first()
    if not level:
        raise HTTPException(status_code=404, detail=f"Level {level_code} not found")

    lessons = db.query(Lesson).filter(
        Lesson.cefr_level_id == level.id
    ).order_by(Lesson.unit_number).all()

    return lessons

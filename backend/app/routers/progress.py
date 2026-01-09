"""
Progress tracking API endpoints.
"""
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional
from datetime import datetime, timedelta

from ..database import get_db
from ..models import User, UserProgress, PracticeSession, Vocabulary, Grammar, Verb, CEFRLevel
from ..schemas.progress import ProgressResponse, OverallProgress, WeakArea, PracticeSessionResponse
from ..services import SpacedRepetitionService
from ..models.progress import ItemType

router = APIRouter(prefix="/progress", tags=["progress"])


@router.get("/", response_model=OverallProgress)
def get_overall_progress(db: Session = Depends(get_db)):
    """Get overall learning progress."""
    user = db.query(User).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Get current level
    current_level = user.current_cefr_level

    # Count learned vocabulary (items with at least 1 correct answer)
    vocab_learned = db.query(UserProgress).filter(
        UserProgress.user_id == user.id,
        UserProgress.item_type == ItemType.VOCABULARY,
        UserProgress.correct_count > 0
    ).count()

    # Get total vocabulary for current level and below
    level = db.query(CEFRLevel).filter(CEFRLevel.code == current_level).first()
    if level:
        vocab_total = db.query(Vocabulary).filter(
            Vocabulary.cefr_level_id <= level.id
        ).count()
    else:
        vocab_total = db.query(Vocabulary).count()

    # Count grammar topics
    grammar_learned = db.query(UserProgress).filter(
        UserProgress.user_id == user.id,
        UserProgress.item_type == ItemType.GRAMMAR,
        UserProgress.correct_count > 0
    ).count()

    grammar_total = db.query(Grammar).count()

    # Count verbs
    verbs_learned = db.query(UserProgress).filter(
        UserProgress.user_id == user.id,
        UserProgress.item_type == ItemType.VERB,
        UserProgress.correct_count > 0
    ).count()

    verbs_total = db.query(Verb).count()

    # Calculate total practice time
    total_time = db.query(func.sum(PracticeSession.actual_duration_mins)).filter(
        PracticeSession.user_id == user.id,
        PracticeSession.completed_at.isnot(None)
    ).scalar() or 0

    # Calculate streak (consecutive days with practice)
    today = datetime.now().date()
    streak = 0
    check_date = today

    while True:
        has_practice = db.query(PracticeSession).filter(
            PracticeSession.user_id == user.id,
            func.date(PracticeSession.started_at) == check_date
        ).first()

        if has_practice:
            streak += 1
            check_date -= timedelta(days=1)
        else:
            break

    # 7-day accuracy
    week_ago = datetime.now() - timedelta(days=7)
    recent_sessions = db.query(PracticeSession).filter(
        PracticeSession.user_id == user.id,
        PracticeSession.started_at >= week_ago
    ).all()

    total_correct = sum(s.correct_count or 0 for s in recent_sessions)
    total_answered = sum((s.correct_count or 0) + (s.incorrect_count or 0) for s in recent_sessions)
    accuracy_7_days = (total_correct / total_answered * 100) if total_answered > 0 else 0

    # Items due for review
    items_due = SpacedRepetitionService.get_items_due_for_review(db, user.id)

    return OverallProgress(
        current_level=current_level,
        vocabulary_learned=vocab_learned,
        vocabulary_total=vocab_total,
        grammar_learned=grammar_learned,
        grammar_total=grammar_total,
        verbs_learned=verbs_learned,
        verbs_total=verbs_total,
        total_practice_time_mins=total_time,
        current_streak_days=streak,
        accuracy_7_days=round(accuracy_7_days, 1),
        items_due_for_review=len(items_due)
    )


@router.get("/weak-areas", response_model=List[WeakArea])
def get_weak_areas(
    limit: int = Query(10, ge=1, le=50),
    db: Session = Depends(get_db)
):
    """Get areas where user needs more practice."""
    user = db.query(User).first()
    if not user:
        return []

    weak_items = SpacedRepetitionService.get_weak_items(db, user.id, limit=limit)

    weak_areas = []
    for item in weak_items:
        if item.item_type == ItemType.VOCABULARY:
            vocab = db.query(Vocabulary).filter(Vocabulary.id == item.item_id).first()
            if vocab:
                weak_areas.append(WeakArea(
                    area_type="vocabulary",
                    area_name=vocab.french,
                    accuracy=item.accuracy,
                    last_practiced=item.last_reviewed,
                    recommended_exercises=3
                ))
        elif item.item_type == ItemType.VERB:
            verb = db.query(Verb).filter(Verb.id == item.item_id).first()
            if verb:
                weak_areas.append(WeakArea(
                    area_type="verb",
                    area_name=verb.infinitive,
                    accuracy=item.accuracy,
                    last_practiced=item.last_reviewed,
                    recommended_exercises=5
                ))

    return weak_areas


@router.get("/due-for-review", response_model=List[ProgressResponse])
def get_items_due_for_review(
    item_type: Optional[str] = Query(None, description="Filter by type (vocabulary, grammar, verb)"),
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db)
):
    """Get items that are due for spaced repetition review."""
    user = db.query(User).first()
    if not user:
        return []

    type_map = {
        "vocabulary": ItemType.VOCABULARY,
        "grammar": ItemType.GRAMMAR,
        "verb": ItemType.VERB,
    }

    filter_type = type_map.get(item_type) if item_type else None

    items = SpacedRepetitionService.get_items_due_for_review(
        db, user.id, item_type=filter_type, limit=limit
    )

    return [ProgressResponse.model_validate(item) for item in items]


@router.get("/sessions", response_model=List[PracticeSessionResponse])
def get_practice_sessions(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """Get practice session history."""
    user = db.query(User).first()
    if not user:
        return []

    sessions = db.query(PracticeSession).filter(
        PracticeSession.user_id == user.id
    ).order_by(PracticeSession.started_at.desc()).offset(skip).limit(limit).all()

    return [PracticeSessionResponse.model_validate(s) for s in sessions]


@router.get("/item/{item_type}/{item_id}", response_model=ProgressResponse)
def get_item_progress(
    item_type: str,
    item_id: int,
    db: Session = Depends(get_db)
):
    """Get progress for a specific item."""
    user = db.query(User).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    type_map = {
        "vocabulary": ItemType.VOCABULARY,
        "grammar": ItemType.GRAMMAR,
        "verb": ItemType.VERB,
    }

    if item_type not in type_map:
        raise HTTPException(status_code=400, detail="Invalid item type")

    progress = db.query(UserProgress).filter(
        UserProgress.user_id == user.id,
        UserProgress.item_type == type_map[item_type],
        UserProgress.item_id == item_id
    ).first()

    if not progress:
        raise HTTPException(status_code=404, detail="No progress found for this item")

    return ProgressResponse.model_validate(progress)

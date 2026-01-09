"""
Vocabulary API endpoints.
"""
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from ..database import get_db
from ..models import Vocabulary, CEFRLevel
from ..schemas import VocabularyResponse, VocabularyDetail

router = APIRouter(prefix="/vocabulary", tags=["vocabulary"])


@router.get("/", response_model=List[VocabularyResponse])
def get_vocabulary(
    level: Optional[str] = Query(None, description="Filter by CEFR level"),
    category: Optional[str] = Query(None, description="Filter by category"),
    part_of_speech: Optional[str] = Query(None, description="Filter by part of speech"),
    cognates_only: bool = Query(False, description="Show only cognates"),
    search: Optional[str] = Query(None, description="Search in French/English"),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db)
):
    """Get vocabulary items with optional filters."""
    query = db.query(Vocabulary)

    if level:
        cefr_level = db.query(CEFRLevel).filter(CEFRLevel.code == level.upper()).first()
        if cefr_level:
            query = query.filter(Vocabulary.cefr_level_id == cefr_level.id)

    if category:
        query = query.filter(Vocabulary.category == category)

    if part_of_speech:
        query = query.filter(Vocabulary.part_of_speech == part_of_speech)

    if cognates_only:
        query = query.filter(Vocabulary.is_cognate == True)

    if search:
        search_term = f"%{search}%"
        query = query.filter(
            (Vocabulary.french.ilike(search_term)) |
            (Vocabulary.english.ilike(search_term))
        )

    vocabulary = query.offset(skip).limit(limit).all()
    return vocabulary


@router.get("/categories")
def get_categories(
    level: Optional[str] = Query(None, description="Filter by CEFR level"),
    db: Session = Depends(get_db)
):
    """Get all vocabulary categories."""
    query = db.query(Vocabulary.category).distinct()

    if level:
        cefr_level = db.query(CEFRLevel).filter(CEFRLevel.code == level.upper()).first()
        if cefr_level:
            query = query.filter(Vocabulary.cefr_level_id == cefr_level.id)

    categories = [c[0] for c in query.all() if c[0]]
    return {"categories": sorted(categories)}


@router.get("/{vocab_id}", response_model=VocabularyDetail)
def get_vocabulary_item(vocab_id: int, db: Session = Depends(get_db)):
    """Get a specific vocabulary item by ID."""
    vocab = db.query(Vocabulary).filter(Vocabulary.id == vocab_id).first()
    if not vocab:
        raise HTTPException(status_code=404, detail="Vocabulary item not found")
    return vocab


@router.get("/random/{count}", response_model=List[VocabularyResponse])
def get_random_vocabulary(
    count: int,
    level: Optional[str] = Query(None, description="Filter by CEFR level"),
    db: Session = Depends(get_db)
):
    """Get random vocabulary items for practice."""
    from sqlalchemy.sql.expression import func

    query = db.query(Vocabulary)

    if level:
        cefr_level = db.query(CEFRLevel).filter(CEFRLevel.code == level.upper()).first()
        if cefr_level:
            query = query.filter(Vocabulary.cefr_level_id == cefr_level.id)

    vocabulary = query.order_by(func.random()).limit(count).all()
    return vocabulary

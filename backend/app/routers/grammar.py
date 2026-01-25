"""
Grammar API endpoints.
"""
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from ..database import get_db
from ..models import Grammar, CEFRLevel
from ..schemas import GrammarResponse, GrammarDetail

router = APIRouter(prefix="/grammar", tags=["grammar"])


@router.get("/", response_model=List[GrammarDetail])
def get_grammar_topics(
    level: Optional[str] = Query(None, description="Filter by CEFR level"),
    db: Session = Depends(get_db)
):
    """Get all grammar topics, optionally filtered by level."""
    query = db.query(Grammar)

    if level:
        cefr_level = db.query(CEFRLevel).filter(CEFRLevel.code == level.upper()).first()
        if cefr_level:
            query = query.filter(Grammar.cefr_level_id == cefr_level.id)

    grammar = query.order_by(Grammar.cefr_level_id, Grammar.order).all()
    return grammar


@router.get("/{grammar_id}", response_model=GrammarDetail)
def get_grammar_topic(grammar_id: int, db: Session = Depends(get_db)):
    """Get a specific grammar topic by ID."""
    grammar = db.query(Grammar).filter(Grammar.id == grammar_id).first()
    if not grammar:
        raise HTTPException(status_code=404, detail="Grammar topic not found")
    return grammar


@router.get("/topic/{topic}", response_model=GrammarDetail)
def get_grammar_by_topic(topic: str, db: Session = Depends(get_db)):
    """Get a grammar topic by its topic slug."""
    grammar = db.query(Grammar).filter(Grammar.topic == topic).first()
    if not grammar:
        raise HTTPException(status_code=404, detail=f"Grammar topic '{topic}' not found")
    return grammar

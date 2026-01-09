"""
Verbs API endpoints.
"""
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from ..database import get_db
from ..models import Verb, VerbConjugation, CEFRLevel
from ..schemas import VerbResponse, VerbDetail, ConjugationResponse

router = APIRouter(prefix="/verbs", tags=["verbs"])


@router.get("/", response_model=List[VerbResponse])
def get_verbs(
    level: Optional[str] = Query(None, description="Filter by CEFR level"),
    group: Optional[int] = Query(None, description="Filter by verb group (1, 2, 3)"),
    irregular_only: bool = Query(False, description="Show only irregular verbs"),
    search: Optional[str] = Query(None, description="Search verb infinitive"),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db)
):
    """Get verbs with optional filters."""
    query = db.query(Verb)

    if level:
        cefr_level = db.query(CEFRLevel).filter(CEFRLevel.code == level.upper()).first()
        if cefr_level:
            query = query.filter(Verb.cefr_level_id == cefr_level.id)

    if group:
        query = query.filter(Verb.group == group)

    if irregular_only:
        query = query.filter(Verb.is_irregular == True)

    if search:
        query = query.filter(Verb.infinitive.ilike(f"%{search}%"))

    verbs = query.offset(skip).limit(limit).all()
    return verbs


@router.get("/{verb_id}", response_model=VerbDetail)
def get_verb(verb_id: int, db: Session = Depends(get_db)):
    """Get a specific verb with all conjugations."""
    verb = db.query(Verb).filter(Verb.id == verb_id).first()
    if not verb:
        raise HTTPException(status_code=404, detail="Verb not found")

    # Manually construct response with conjugations
    conjugations = db.query(VerbConjugation).filter(
        VerbConjugation.verb_id == verb_id
    ).all()

    response = VerbDetail(
        id=verb.id,
        infinitive=verb.infinitive,
        english=verb.english,
        spanish=verb.spanish,
        group=verb.group.value,
        is_irregular=verb.is_irregular,
        cefr_level_id=verb.cefr_level_id,
        auxiliary=verb.auxiliary.value,
        past_participle=verb.past_participle,
        present_participle=verb.present_participle,
        notes=verb.notes,
        is_reflexive=verb.is_reflexive,
        spanish_comparison=verb.spanish_comparison,
        conjugations=[ConjugationResponse.model_validate(c) for c in conjugations]
    )

    return response


@router.get("/infinitive/{infinitive}", response_model=VerbDetail)
def get_verb_by_infinitive(infinitive: str, db: Session = Depends(get_db)):
    """Get a verb by its infinitive form."""
    verb = db.query(Verb).filter(Verb.infinitive == infinitive.lower()).first()
    if not verb:
        raise HTTPException(status_code=404, detail=f"Verb '{infinitive}' not found")

    conjugations = db.query(VerbConjugation).filter(
        VerbConjugation.verb_id == verb.id
    ).all()

    response = VerbDetail(
        id=verb.id,
        infinitive=verb.infinitive,
        english=verb.english,
        spanish=verb.spanish,
        group=verb.group.value,
        is_irregular=verb.is_irregular,
        cefr_level_id=verb.cefr_level_id,
        auxiliary=verb.auxiliary.value,
        past_participle=verb.past_participle,
        present_participle=verb.present_participle,
        notes=verb.notes,
        is_reflexive=verb.is_reflexive,
        spanish_comparison=verb.spanish_comparison,
        conjugations=[ConjugationResponse.model_validate(c) for c in conjugations]
    )

    return response


@router.get("/{verb_id}/conjugations", response_model=List[ConjugationResponse])
def get_verb_conjugations(
    verb_id: int,
    tense: Optional[str] = Query(None, description="Filter by tense"),
    mood: Optional[str] = Query(None, description="Filter by mood"),
    db: Session = Depends(get_db)
):
    """Get conjugations for a specific verb."""
    query = db.query(VerbConjugation).filter(VerbConjugation.verb_id == verb_id)

    if tense:
        query = query.filter(VerbConjugation.tense == tense)

    if mood:
        query = query.filter(VerbConjugation.mood == mood)

    conjugations = query.all()
    return conjugations

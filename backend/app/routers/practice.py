"""
Practice session API endpoints.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
import unicodedata

from ..database import get_db
from ..models import PracticeSession, User
from ..schemas import (
    PracticeSessionCreate,
    PracticeSessionResponse,
    AnswerSubmit,
    AnswerResult,
    ExerciseResponse
)
from ..services import ExerciseGenerator, SpacedRepetitionService
from ..models.progress import ItemType

router = APIRouter(prefix="/practice", tags=["practice"])

# Store active sessions (in production, use Redis or similar)
active_sessions: dict = {}


@router.post("/start", response_model=dict)
def start_practice_session(
    session_config: PracticeSessionCreate,
    db: Session = Depends(get_db)
):
    """Start a new practice session."""
    # Get or create default user
    user = db.query(User).first()
    if not user:
        user = User(
            name="French Learner",
            native_language="en-US",
            secondary_language="es-ES",
            current_cefr_level="A1"
        )
        db.add(user)
        db.commit()
        db.refresh(user)

    # Create session record
    session = PracticeSession(
        user_id=user.id,
        session_type=session_config.session_type,
        target_duration_mins=session_config.duration_mins,
        focus_areas=session_config.focus_areas,
        started_at=datetime.now()
    )
    db.add(session)
    db.commit()
    db.refresh(session)

    # Generate exercises for the session
    generator = ExerciseGenerator(db)
    cefr_level = session_config.cefr_level or user.current_cefr_level

    # Calculate number of exercises based on duration (roughly 1 per minute)
    exercise_count = session_config.duration_mins

    exercises = generator.generate_exercise_set(
        user_id=user.id,
        count=exercise_count,
        cefr_level=cefr_level,
        focus_areas=session_config.focus_areas
    )

    # Store in active sessions
    active_sessions[session.id] = {
        "session": session,
        "exercises": exercises,
        "current_index": 0,
        "answers": []
    }

    return {
        "session_id": session.id,
        "total_exercises": len(exercises),
        "duration_mins": session_config.duration_mins,
        "focus_areas": session_config.focus_areas
    }


@router.get("/{session_id}/next")
def get_next_exercise(session_id: int, db: Session = Depends(get_db)):
    """Get the next exercise in the session."""
    if session_id not in active_sessions:
        raise HTTPException(status_code=404, detail="Session not found or expired")

    session_data = active_sessions[session_id]
    exercises = session_data["exercises"]
    current_index = session_data["current_index"]

    if current_index >= len(exercises):
        return {
            "complete": True,
            "message": "Session complete!",
            "total": len(exercises),
            "correct": sum(1 for a in session_data["answers"] if a.get("correct", False))
        }

    exercise = exercises[current_index]

    return {
        "complete": False,
        "exercise_index": current_index,
        "total_exercises": len(exercises),
        "exercise": {
            "type": exercise["type"],
            "content": exercise["content"],
        }
    }


@router.post("/{session_id}/answer")
def submit_answer(
    session_id: int,
    answer: AnswerSubmit,
    db: Session = Depends(get_db)
):
    """Submit an answer for the current exercise."""
    if session_id not in active_sessions:
        raise HTTPException(status_code=404, detail="Session not found or expired")

    session_data = active_sessions[session_id]
    current_index = session_data["current_index"]
    exercises = session_data["exercises"]

    if current_index >= len(exercises):
        raise HTTPException(status_code=400, detail="Session already complete")

    current_exercise = exercises[current_index]
    correct_answer = current_exercise["answer"]

    # Check if answer is correct (simplified - varies by exercise type)
    is_correct = check_answer(
        exercise_type=current_exercise["type"],
        user_answer=answer.answer,
        correct_answer=correct_answer
    )

    # Record the answer
    session_data["answers"].append({
        "exercise_index": current_index,
        "user_answer": answer.answer,
        "correct_answer": correct_answer,
        "correct": is_correct,
        "time_taken": answer.time_taken_seconds
    })

    # Update progress using spaced repetition
    user = db.query(User).first()
    if user and "vocabulary_id" in current_exercise.get("content", {}):
        SpacedRepetitionService.update_progress(
            db=db,
            user_id=user.id,
            item_type=ItemType.VOCABULARY,
            item_id=current_exercise["content"]["vocabulary_id"],
            correct=is_correct,
            time_taken_seconds=answer.time_taken_seconds
        )

    # Move to next exercise
    session_data["current_index"] += 1

    # Update session stats
    session = db.query(PracticeSession).filter(PracticeSession.id == session_id).first()
    if session:
        session.items_practiced = session_data["current_index"]
        if is_correct:
            session.correct_count = (session.correct_count or 0) + 1
        else:
            session.incorrect_count = (session.incorrect_count or 0) + 1
        db.commit()

    return AnswerResult(
        correct=is_correct,
        correct_answer=correct_answer,
        explanation=current_exercise.get("explanation"),
        spanish_note=current_exercise.get("content", {}).get("spanish_hint"),
        points_earned=10 if is_correct else 0,
        streak=count_streak(session_data["answers"])
    )


@router.post("/{session_id}/complete")
def complete_session(session_id: int, db: Session = Depends(get_db)):
    """Complete and close a practice session."""
    if session_id not in active_sessions:
        raise HTTPException(status_code=404, detail="Session not found or expired")

    session_data = active_sessions[session_id]

    # Update session in database
    session = db.query(PracticeSession).filter(PracticeSession.id == session_id).first()
    if session:
        session.completed_at = datetime.now()
        session.items_practiced = len(session_data["answers"])
        session.correct_count = sum(1 for a in session_data["answers"] if a.get("correct", False))
        session.incorrect_count = sum(1 for a in session_data["answers"] if not a.get("correct", False))

        # Calculate actual duration
        if session.started_at:
            delta = datetime.now() - session.started_at
            session.actual_duration_mins = int(delta.total_seconds() / 60)

        db.commit()
        db.refresh(session)

    # Clean up active session
    del active_sessions[session_id]

    return PracticeSessionResponse.model_validate(session)


@router.get("/{session_id}/summary")
def get_session_summary(session_id: int, db: Session = Depends(get_db)):
    """Get summary of a completed session."""
    session = db.query(PracticeSession).filter(PracticeSession.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    return PracticeSessionResponse.model_validate(session)


def check_answer(exercise_type: str, user_answer, correct_answer: dict) -> bool:
    """Check if user's answer is correct based on exercise type."""
    if exercise_type == "vocabulary_flashcard":
        # Check if user typed the correct translation
        expected = correct_answer.get("french", "").lower().strip()
        user = str(user_answer).lower().strip()
        return user == expected or user in expected

    elif exercise_type == "multiple_choice":
        return user_answer == correct_answer.get("correct_index")

    elif exercise_type == "gender":
        return str(user_answer).lower() == correct_answer.get("correct_article", "").lower()

    elif exercise_type == "conjugation":
        expected = correct_answer.get("correct_answer", "").lower().strip()
        user = str(user_answer).lower().strip()
        return user == expected

    elif exercise_type == "sentence_builder":
        expected = correct_answer.get("correct_order", [])
        if isinstance(user_answer, list):
            return user_answer == expected
        return False

    elif exercise_type == "listening":
        # Listening is multiple choice - compare index
        return user_answer == correct_answer.get("correct_index")

    elif exercise_type in ("speaking", "pronunciation"):
        # Compare spoken text with expected text using similarity
        expected = correct_answer.get("expected_text", "").lower().strip()
        user = str(user_answer).lower().strip()
        # Normalize: remove accents and punctuation for comparison
        def normalize(s):
            # Remove accents
            s = unicodedata.normalize('NFD', s)
            s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
            # Remove punctuation and extra spaces
            s = ''.join(c for c in s if c.isalnum() or c.isspace())
            return ' '.join(s.split())

        norm_expected = normalize(expected)
        norm_user = normalize(user)

        # Exact match after normalization
        if norm_expected == norm_user:
            return True

        # Calculate similarity (simple Levenshtein-like approach)
        # Allow 80% similarity threshold
        if not norm_expected or not norm_user:
            return False

        # Simple word-based matching
        expected_words = set(norm_expected.split())
        user_words = set(norm_user.split())
        if not expected_words:
            return False

        common_words = expected_words.intersection(user_words)
        similarity = len(common_words) / len(expected_words)
        return similarity >= 0.7  # 70% of words match

    return False


def count_streak(answers: list) -> int:
    """Count current streak of correct answers."""
    streak = 0
    for answer in reversed(answers):
        if answer.get("correct", False):
            streak += 1
        else:
            break
    return streak

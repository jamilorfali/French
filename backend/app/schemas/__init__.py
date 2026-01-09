"""
Pydantic schemas for API request/response validation.
"""
from .user import UserBase, UserCreate, UserUpdate, UserResponse
from .cefr_level import CEFRLevelResponse
from .lesson import LessonResponse, LessonDetail
from .vocabulary import VocabularyResponse, VocabularyDetail
from .grammar import GrammarResponse, GrammarDetail
from .verb import VerbResponse, VerbDetail, ConjugationResponse
from .exercise import ExerciseResponse, ExerciseContent
from .progress import (
    ProgressResponse,
    PracticeSessionCreate,
    PracticeSessionResponse,
    AnswerSubmit,
    AnswerResult
)

__all__ = [
    "UserBase", "UserCreate", "UserUpdate", "UserResponse",
    "CEFRLevelResponse",
    "LessonResponse", "LessonDetail",
    "VocabularyResponse", "VocabularyDetail",
    "GrammarResponse", "GrammarDetail",
    "VerbResponse", "VerbDetail", "ConjugationResponse",
    "ExerciseResponse", "ExerciseContent",
    "ProgressResponse", "PracticeSessionCreate", "PracticeSessionResponse",
    "AnswerSubmit", "AnswerResult",
]

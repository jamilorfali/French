"""
API Routers.
"""
from .levels import router as levels_router
from .lessons import router as lessons_router
from .vocabulary import router as vocabulary_router
from .grammar import router as grammar_router
from .verbs import router as verbs_router
from .practice import router as practice_router
from .progress import router as progress_router
from .user import router as user_router

__all__ = [
    "levels_router",
    "lessons_router",
    "vocabulary_router",
    "grammar_router",
    "verbs_router",
    "practice_router",
    "progress_router",
    "user_router",
]

"""
FrenchFlow - French Language Learning Application

Main FastAPI application entry point.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from .config import settings
from .database import init_db
from .routers import (
    levels_router,
    lessons_router,
    vocabulary_router,
    grammar_router,
    verbs_router,
    practice_router,
    progress_router,
    user_router,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan handler.
    Initializes database on startup.
    """
    # Startup
    print("🇫🇷 Starting FrenchFlow...")
    init_db()
    print("✅ Database initialized")
    yield
    # Shutdown
    print("👋 FrenchFlow shutting down...")


# Create FastAPI application
app = FastAPI(
    title=settings.app_name,
    description="""
    FrenchFlow - Personal French Language Learning Application

    A comprehensive learning platform for progressing from CEFR A1 to C2,
    leveraging Spanish-French connections for accelerated learning.

    ## Features
    - Vocabulary flashcards with Spanish cognate highlighting
    - Grammar explanations with Spanish comparisons
    - Verb conjugation drills
    - Listening and speaking exercises (via Web Speech API)
    - Spaced repetition for optimal retention
    - Progress tracking and weak area identification

    ## User Profile
    - Native: English (US)
    - Secondary: Spanish (Spain)
    - Target: French
    """,
    version=settings.app_version,
    lifespan=lifespan,
)

# Configure CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for LAN access
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(levels_router, prefix="/api")
app.include_router(lessons_router, prefix="/api")
app.include_router(vocabulary_router, prefix="/api")
app.include_router(grammar_router, prefix="/api")
app.include_router(verbs_router, prefix="/api")
app.include_router(practice_router, prefix="/api")
app.include_router(progress_router, prefix="/api")
app.include_router(user_router, prefix="/api")


@app.get("/")
async def root():
    """Root endpoint - API information."""
    return {
        "name": settings.app_name,
        "version": settings.app_version,
        "description": "French Language Learning Application",
        "docs": "/docs",
        "api": "/api",
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "app": settings.app_name}


@app.get("/api")
async def api_info():
    """API information endpoint."""
    return {
        "endpoints": {
            "levels": "/api/levels - CEFR levels (A1-C2)",
            "lessons": "/api/lessons - Lesson units",
            "vocabulary": "/api/vocabulary - Vocabulary items",
            "grammar": "/api/grammar - Grammar topics",
            "verbs": "/api/verbs - Verbs and conjugations",
            "practice": "/api/practice - Practice sessions",
            "progress": "/api/progress - Learning progress",
            "user": "/api/user - User profile",
        },
        "docs": {
            "swagger": "/docs",
            "redoc": "/redoc",
        }
    }

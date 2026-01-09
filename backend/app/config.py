"""
Application configuration settings.
"""
from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Application
    app_name: str = "FrenchFlow"
    app_version: str = "1.0.0"
    debug: bool = True

    # Server
    host: str = "0.0.0.0"  # Listen on all interfaces for LAN access
    port: int = 8000

    # Database
    database_url: str = "sqlite:///./frenchflow.db"

    # CORS - Allow frontend and LAN access
    cors_origins: list[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5173",  # Vite dev server
        "http://127.0.0.1:5173",
    ]

    # User Profile (pre-configured for your learning profile)
    default_user_name: str = "French Learner"
    default_native_lang: str = "en-US"
    default_secondary_lang: str = "es-ES"
    default_current_level: str = "A1"

    # Practice Settings
    default_session_duration: int = 15  # minutes
    new_content_ratio: float = 0.2  # 20% new, 80% review

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()


# Ensure data directory exists
DATA_DIR = Path(__file__).parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)

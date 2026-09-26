import os
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

# Base directories
BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_PATH = BASE_DIR / ".env"

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(ENV_PATH),
        env_file_encoding="utf-8",
        extra="ignore"
    )

    APP_NAME: str = "PocketSmart AI"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    ENVIRONMENT: str = "development"
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000


    # Security & JWT
    SECRET_KEY: str = "pocketsmart-super-secret-key-change-in-production-2026"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440  # 24 hours

    # Database
    DATABASE_URL: str = f"sqlite:///{BASE_DIR / 'pocketsmart.db'}"

    # Google Gemini API
    GEMINI_API_KEY: str = ""
    GEMINI_MODEL: str = "gemini-1.5-flash"

    # Static & Templates
    TEMPLATES_DIR: Path = BASE_DIR / "frontend" / "templates"
    STATIC_DIR: Path = BASE_DIR / "frontend" / "static"
    UPLOAD_DIR: Path = BASE_DIR / "frontend" / "static" / "uploads"


settings = Settings()

# Ensure uploads directory exists
settings.UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

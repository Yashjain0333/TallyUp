"""Pydantic Settings module for FastAPI App"""

from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None
    MONGO_INITDB_DATABASE: Optional[str] = None
    MONGO_INITDB_ROOT_USERNAME: Optional[str] = None
    MONGO_INITDB_ROOT_PASSWORD: Optional[str] = None
    MONGO_URI: Optional[str] = None
    MONGO_DB: Optional[str] = None
    SECRET_KEY: Optional[str] = None  # Replace with a secure secret key in production
    ALGORITHM: Optional[str] = None
    ACCESS_TOKEN_EXPIRE_MINUTES: Optional[str] = None
    REFRESH_TOKEN_EXPIRE_DAYS: Optional[str] = None

    ALLOWED_ORIGINS: Optional[str] = None

    CLIENT_ORIGIN: Optional[str] = None

    class Config:
        env_file = ".env"
        from_attributes = True


settings = Settings()

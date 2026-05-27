"""Application configuration."""
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    GEMINI_API_KEY: str
    PORT: int = 8000
    APP_NAME: str = "AI Log Investigator"
    DEBUG: bool = True
    model_config = SettingsConfigDict(
        env_file=".env"
    )

settings = Settings()
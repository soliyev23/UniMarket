"""
Конфигурация приложения UniMarket
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "UniMarket"
    VERSION: str = "0.1.0"
    DEBUG: bool = True

    API_PREFIX: str = "/api/v1"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

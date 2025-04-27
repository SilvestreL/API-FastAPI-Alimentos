# app/core/settings.py

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    FIRST_SUPERUSER: str = "admin@example.com"
    FIRST_SUPERUSER_PASSWORD: str = "123456"

    class Config:
        env_file = ".env"


settings = Settings()

# app/core/settings.py

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Banco de Dados
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_port: str

    # Segurança
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    # Superusuário
    FIRST_SUPERUSER: str = "admin@example.com"
    FIRST_SUPERUSER_PASSWORD: str = "123456"

    model_config = SettingsConfigDict(env_file=".env", extra="allow")


settings = Settings()

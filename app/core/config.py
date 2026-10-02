from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "TrabalhAI"
    ENVIRONMENT: str = "development"
    LOG_LEVEL: str = "INFO"

    OPENAI_API_KEY: str = "sk-placeholder"

    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "trabalhai"
    POSTGRES_PASSWORD: str = "trabalhaipassword"
    POSTGRES_DB: str = "trabalhai_db"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
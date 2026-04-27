from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Kata Rene API"
    app_version: str = "0.1.0"
    database_url: str = "sqlite+aiosqlite:///./kata.db"
    debug: bool = False

    class Config:
        env_file = ".env"


settings = Settings()

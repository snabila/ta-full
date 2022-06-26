from pydantic import BaseSettings

class Settings(BaseSettings):
    DB_URL: str
    GATE: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
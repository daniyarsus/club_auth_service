import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASS: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_NAME: str

    REDIS_USER: str
    REDIS_HOST: str
    REDIS_PORT: str
    REDIS_PASS: str

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_ACCESS_TOKEN_EXPIRE_SECONDS: str
    JWT_REFRESH_TOKEN_EXPIRE_SECONDS: str

    SMTP_DOMAIN_NAME: str
    SMTP_PORT: str
    SMTP_API_KEY: str
    SMTP_EMAIL_FROM: str

    class Config:
        env_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")


settings: Settings = Settings()


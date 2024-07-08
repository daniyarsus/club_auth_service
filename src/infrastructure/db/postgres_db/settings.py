from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import sessionmaker

from src.config import settings

POSTGRES_USER = settings.POSTGRES_USER
POSTGRES_PASS = settings.POSTGRES_PASS
POSTGRES_HOST = settings.POSTGRES_HOST
POSTGRES_PORT = settings.POSTGRES_PORT
POSTGRES_NAME = settings.POSTGRES_NAME


async_DB_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_NAME}"

async_engine = create_async_engine(
    url=async_DB_URL,
    echo=False
)

async_session = async_sessionmaker(
    async_engine,
    expire_on_commit=False,
    autocommit=False,
)

sync_DB_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_NAME}"

sync_engine = create_engine(
    url=sync_DB_URL,
    echo=False
)

sync_session = sessionmaker(
    sync_engine,
    expire_on_commit=False,
    autocommit=False,
)

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from src.config import settings


async_DB_URL = f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASS}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_NAME}"

async_engine = create_async_engine(
    url=async_DB_URL,
    echo=False
)

async_session = async_sessionmaker(
    async_engine,
    expire_on_commit=False,
    autocommit=False,
)

sync_DB_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASS}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_NAME}"

sync_engine = create_engine(
    url=sync_DB_URL,
    echo=False
)

sync_session = sessionmaker(
    sync_engine,
    expire_on_commit=False,
    autocommit=False,
)


from src.infrastructure.db.postgres_db.models.base import SQLAlchemyBase
#SQLAlchemyBase.metadata.create_all(bind=sync_engine)

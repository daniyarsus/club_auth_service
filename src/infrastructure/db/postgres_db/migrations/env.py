from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

from src.infrastructure.db.postgres_db.models import *
from src.infrastructure.db.postgres_db.models.base import SQLAlchemyBase
from src.infrastructure.db.postgres_db.settings import (POSTGRES_HOST,
                                                        POSTGRES_NAME,
                                                        POSTGRES_PASS,
                                                        POSTGRES_PORT,
                                                        POSTGRES_USER,
                                                        sync_DB_URL)

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

section = config.config_ini_section
config.set_section_option(section, "DB_USER", POSTGRES_USER)
config.set_section_option(section, "DB_PASS", POSTGRES_PASS)
config.set_section_option(section, "DB_HOST", POSTGRES_HOST)
config.set_section_option(section, "DB_PORT", POSTGRES_PORT)
config.set_section_option(section, "DB_NAME", POSTGRES_NAME)

target_metadata = SQLAlchemyBase.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option(sync_DB_URL)
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, default={}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

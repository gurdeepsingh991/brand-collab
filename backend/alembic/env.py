# alembic/env.py

from logging.config import fileConfig
from alembic import context
from sqlalchemy import engine_from_config, pool
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Inject the correct DB URL into the Alembic config
config = context.config
config.set_main_option("sqlalchemy.url", os.getenv("ALEMBIC_DATABASE_URL"))

# Setup Python logging
if config.config_file_name:
    fileConfig(config.config_file_name)

# ✅ Import Base from the sync-only db_base
from app.db_base import Base

# ✅ Import all models so Alembic sees them
from app.models import (
    user,
    brand,
    campaign,
    influencer,
    collab_applications,
    influencer_platform,
    influencer_service,
    collaboration,
)

target_metadata = Base.metadata


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

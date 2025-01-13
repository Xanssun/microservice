from core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


# Асинхронное подключение
async_dsn = f'postgresql+asyncpg://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}'
async_engine = create_async_engine(async_dsn, echo=True, future=True)
async_session = sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)

async def get_session():
    """Генератор для получения асинхронной сессии."""
    async with async_session() as session:
        yield session

async def purge_database() -> None:
    """Очистка базы данных (асинхронно)."""
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


# Синхронное подключение
sync_dsn = f'postgresql://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}'
sync_engine = create_engine(sync_dsn, echo=True, future=True)
sync_session = sessionmaker(
    sync_engine, autocommit=False, autoflush=False
)

def get_sync_session():
    """Генератор для получения синхронной сессии."""
    with sync_session() as session:
        yield session

def get_db_session():
    """Фабрика для получения синхронной сессии."""
    return next(get_sync_session())

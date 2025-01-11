from core.config import settings
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


dsn = f'postgresql+asyncpg://{settings.db_user}:\
    {settings.db_password}@{settings.db_host}:\
    {settings.db_port}/{settings.db_name}'

async_engine = create_async_engine(dsn, echo=True, future=True)
async_session = sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)

async def get_session():
    async with async_session() as session:
        yield session


async def purge_database() -> None:
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

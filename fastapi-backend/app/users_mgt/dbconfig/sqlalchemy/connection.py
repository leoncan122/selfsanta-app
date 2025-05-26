from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
DB_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/postgres"
db_engine = create_async_engine(DB_URL, future=True,echo=True)
AsyncSessionLocal = sessionmaker(db_engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

import os
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

env = load_dotenv()

SQLALCHAMY_DATABASE_URL = os.getenv('SQLALCHAMY_DATABASE_URL')


engine = create_async_engine(SQLALCHAMY_DATABASE_URL)
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db():
    async with async_session() as session:
        yield session

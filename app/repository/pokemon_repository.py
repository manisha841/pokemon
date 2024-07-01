from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import Pokemon

async def get_pokemons(db: AsyncSession):
    result = await db.execute(select(Pokemon))
    return result.scalars().all()

async def get_pokemons_by_name(db: AsyncSession, name: str):
    result = await db.execute(select(Pokemon).where(Pokemon.name.ilike(f"%{name}%")))
    return result.scalars().all()

async def get_pokemons_by_type(db: AsyncSession, type_: str):
    result = await db.execute(select(Pokemon).where(Pokemon.type.ilike(f"%{type_}%")))
    return result.scalars().all()

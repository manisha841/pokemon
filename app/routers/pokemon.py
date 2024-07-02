from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.repository import pokemon_repository

router = APIRouter()


@router.get("/pokemons")
async def read_pokemons(name: str = None, type_: str = None, db: AsyncSession = Depends(get_db)):
    if name and type_:
        pokemons = await pokemon_repository.get_pokemons_by_name_and_type(db=db, name=name, type_=type_)
    elif name:
        pokemons = await pokemon_repository.get_pokemons_by_name(db, name)
    elif type_:
        pokemons = await pokemon_repository.get_pokemons_by_type(db, type_)
    else:
        pokemons = await pokemon_repository.get_pokemons(db)
    if not pokemons:
        raise HTTPException(status_code=404, detail="Pokemons not found")
    return pokemons

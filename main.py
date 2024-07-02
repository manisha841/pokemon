import requests
from fastapi import FastAPI
from app.models import Pokemon, Base
from app.database import engine, async_session
from app.routers import pokemon


app = FastAPI()

app.include_router(pokemon.router, prefix="/api/v1")

async def fetch_and_store_pokemons():
    async with async_session() as session:
        async with session.begin():
            response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=1000")
            data = response.json()
            for item in data['results']:
                details = requests.get(item['url']).json()
                for type_info in details['types']:
                    pokemon = Pokemon(
                        name=details['name'],
                        image=details['sprites']['front_default'],
                        type=type_info['type']['name']
                    )
                    session.add(pokemon)
            await session.commit()

@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await fetch_and_store_pokemons()

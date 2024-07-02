import asyncio
import httpx
from app.database import engine, async_session
from app.models import Base, Pokemon

async def fetch_and_store_pokemons():
    async with async_session() as session:
        async with session.begin():
            async with httpx.AsyncClient() as client:
                response = await client.get("https://pokeapi.co/api/v2/pokemon?limit=5")
                data = response.json()
                for item in data['results']:
                    details = (await client.get(item['url'])).json()
                    for type_info in details['types']:
                        pokemon = Pokemon(
                            name=details['name'],
                            image=details['sprites']['front_default'],
                            type=type_info['type']['name']
                        )
                        session.add(pokemon)
                await session.commit()

async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await fetch_and_store_pokemons()

if __name__ == "__main__":
    asyncio.run(main())

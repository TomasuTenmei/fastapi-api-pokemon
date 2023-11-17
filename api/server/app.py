from fastapi import FastAPI

from server.routes.pokemon import router as PokemonRouter
from server.routes.pkTypes import router as PkTypesRouter
from server.routes.learnset import router as LearnsetRouter

app = FastAPI()

app.include_router(PokemonRouter, tags=["Pokemon"], prefix="/pokemon")
app.include_router(PkTypesRouter, tags=["PkTypes"], prefix="/pkTypes")
app.include_router(LearnsetRouter, tags=["Learnset"], prefix="/learnset")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Bienvenue sur le Pokedex !"}

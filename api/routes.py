from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models import Pokemon, PokemonUpdate

router = APIRouter()

@router.post("/", response_description="Ajouter un nouveau pokémon", status_code=status.HTTP_201_CREATED, response_model=Pokemon)
def create_pokemon(request: Request, pokemon: Pokemon = Body(...)):
    pokemon = jsonable_encoder(pokemon)
    new_pokemon = request.app.database["pokemon"].insert_one(pokemon)
    created_pokemon = request.app.database["pokemon"].find_one(
        {"_id": new_pokemon.inserted_id}
    )
    
    return created_pokemon

@router.get("/", response_description="Liste des pokémons", response_model=List[Pokemon])
def list_pokemon(request: Request):
    pokemons = list(request.app.database["pokemon"].find())
    
    return pokemons

@router.get("/{id}", response_description="Détails d'un pokémon", response_model=Pokemon)
def show_pokemon(request: Request, id: str):
    if (pokemon := request.app.database["pokemon"].find_one({"_id": id})) is not None:
        return pokemon
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Le pokémon {id} n'existe pas.")
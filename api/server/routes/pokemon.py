from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.mongoDB import (
    add_pokemon,
    delete_pokemon,
    retrieve_pokemon,
    retrieve_pokemons,
    update_pokemon,
)
from server.models.pokemon import (
    Pokemon,
    PokemonUpdate,
    ResponseModel
)

router = APIRouter()

@router.post("/", response_description="Ajout d’un pokémon")
async def add_pokemon_data(pokemon: Pokemon = Body(...)):
    pokemon = jsonable_encoder(pokemon)
    new_pokemon = await add_pokemon(pokemon)
    return ResponseModel(new_pokemon, "Pokemon ajouté avec succès.")

@router.get("/", response_description="Liste des pokémons")
async def get_pokemons():
    pokemons = await retrieve_pokemons()
    if pokemons:
        return ResponseModel(pokemons, "Liste des pokémons récupérée avec succès.")
    return ResponseModel(pokemons, "Liste des pokémons vide.")

@router.get("/{id}", response_description="Détails d’un pokémon")
async def get_pokemon_data(id):
    pokemon = await retrieve_pokemon(id)
    if pokemon:
        return ResponseModel(pokemon, "Pokemon récupéré avec succès.")
    return ResponseModel(pokemon, "Aucun pokemon trouvé.")

@router.put("/{id}")
async def update_pokemon_data(id: str, req: PokemonUpdate = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_pokemon = await update_pokemon(id, req)
    if updated_pokemon:
        return ResponseModel(
            "Pokemon avec ID: {} mis à jour avec succès.".format(id),
            "Pokemon mis à jour avec succès."
        )
    return ResponseModel(
        "Impossible de mettre à jour le pokemon avec ID: {}".format(id),
        "Mise à jour du pokemon impossible."
    )
    
@router.delete("/{id}", response_description="Suppression d’un pokémon")
async def delete_pokemon_data(id: str):
    deleted_pokemon = await delete_pokemon(id)
    if deleted_pokemon:
        return ResponseModel(
            "Pokemon avec ID: {} supprimé avec succès.".format(id),
            "Pokemon supprimé avec succès."
        )
    return ResponseModel(
        "Impossible de supprimer le pokemon avec ID: {}".format(id),
        "Suppression du pokemon impossible."
    )

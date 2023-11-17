import motor.motor_asyncio
from bson.objectid import ObjectId

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
db = client.pokedex
pokemon_collection = db.get_collection("pokemon")
pkTypes_collection = db.get_collection("type")
learnset_collection = db.get_collection("learnset")

print("Connecté à la base de données !")

def pokemon_helper(pokemon) -> dict:
    return {
        "id": str(pokemon["_id"]),
        "number": pokemon["number"],
        "name": pokemon["name"],
        "size": pokemon["size"],
        "weight": pokemon["weight"],
        "statistic": pokemon["statistic"],
        "image": pokemon["image"],
        "type": pokemon["type"],
        "learnset": pokemon["learnset"]
    }

def type_helper(type) -> dict:
    return {
        "id": str(type["_id"]),
        "name": type["name"]
    }
    
def learnset_helper(learnset) -> dict:
    return {
        "id": str(learnset["_id"]),
        "name": learnset["name"],
        "description": learnset["description"],
        "power": learnset["power"],
        "precision": learnset["precision"],
        "pp": learnset["pp"],
        "type": learnset["type"]
    }

# 1. GET - /api/pokemons : Récupère la liste de tous les pokémons
async def retrieve_pokemons():
    pokemons = []
    async for pokemon in pokemon_collection.find():
        pokemons.append(pokemon_helper(pokemon))
    return pokemons

# 2. GET - /api/pokemons/:id : Récupère les détails du pokémon précisé par :id
async def retrieve_pokemon(id: str) -> dict:
    pokemon = await pokemon_collection.find_one({"_id": ObjectId(id)})
    if pokemon:
        return pokemon_helper(pokemon)

# 3. GET - /api/types/:id : Récupère les détails du type précisé par :id
async def retrieve_type(id: str) -> dict:
    type = await pkTypes_collection.find_one({"_id": ObjectId(id)})
    if type:
        return type_helper(type)

# 4. GET - /api/abilities : Récupère la liste de toutes les compétences
async def retrieve_learnsets():
    learnsets = []
    async for learnset in learnset_collection.find():
        learnsets.append(learnset_helper(learnset))
    return learnsets

# 5. POST - /api/pokemons : Ajout d’un pokémon
async def add_pokemon(pokemon_data: dict) -> dict:
    pokemon = await pokemon_collection.insert_one(pokemon_data)
    new_pokemon = await pokemon_collection.find_one({"_id": pokemon.inserted_id})
    return pokemon_helper(new_pokemon)

# 6. POST - /api/types : Ajout d’un type
async def add_type(type_data: dict) -> dict:
    type = await pkTypes_collection.insert_one(type_data)
    new_type = await pkTypes_collection.find_one({"_id": type.inserted_id})
    return type_helper(new_type)

# 7. PUT - /api/pokemons/:id : Modification du pokémon précisé par :id
async def update_pokemon(id: str, data: dict):
    if len(data) < 1:
        return False
    pokemon = await pokemon_collection.find_one({"_id": ObjectId(id)})
    if pokemon:
        updated_pokemon = await pokemon_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_pokemon:
            return True
        return False

# 8. PUT - /api/abilities/:id : Modification de la compétence précisé par :id
async def update_learnset(id: str, data: dict):
    if len(data) < 1:
        return False
    learnset = await learnset_collection.find_one({"_id": ObjectId(id)})
    if learnset:
        updated_learnset = await learnset_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_learnset:
            return True
        return False

# 9. PUT - /api/type/:id : Modification du type précisé par :id
async def update_type(id: str, data: dict):
    if len(data) < 1:
        return False
    type = await pkTypes_collection.find_one({"_id": ObjectId(id)})
    if type:
        updated_type = await pkTypes_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_type:
            return True
        return False

# 10. DELETE - /api/pokemons/:id : Supression du pokémon précisé par :id
async def delete_pokemon(id: str):
    pokemon = await pokemon_collection.find_one({"_id": ObjectId(id)})
    if pokemon:
        await pokemon_collection.delete_one({"_id": ObjectId(id)})
        return True

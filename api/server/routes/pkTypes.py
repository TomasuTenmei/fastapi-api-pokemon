from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.mongoDB import (
    add_type,
    retrieve_type,
    update_type,
)
from server.models.pkTypes import (
    PkTypes,
    PkTypesUpdate,
    ResponseModel
)

router = APIRouter()

@router.post("/", response_description="Ajout d’un type")
async def add_type_data(type: PkTypes = Body(...)):
    type = jsonable_encoder(type)
    new_type = await add_type(type)
    return ResponseModel(new_type, "Type ajouté avec succès.")

@router.get("/{id}", response_description="Détails d’un type")
async def get_type_data(id):
    type = await retrieve_type(id)
    if type:
        return ResponseModel(type, "Type récupéré avec succès.")
    return ResponseModel(type, "Aucun type trouvé.")

@router.put("/{id}")
async def update_type_data(id: str, req: PkTypesUpdate = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_type = await update_type(id, req)
    if updated_type:
        return ResponseModel(
            "Type avec ID: {} mis à jour avec succès.".format(id),
            "Type mis à jour avec succès."
        )
    return ResponseModel(
        "Impossible de mettre à jour le type avec ID: {}".format(id),
        "Mise à jour du type impossible."
    )

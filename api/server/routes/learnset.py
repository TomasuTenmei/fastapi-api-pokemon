from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.mongoDB import (
    retrieve_learnsets,
    update_learnset
)
from server.models.learnset import (
    Learnset,
    LearnsetUpdate,
    ResponseModel
)

router = APIRouter()

@router.get("/", response_description="Liste des compétences")
async def get_learnsets():
    learnsets = await retrieve_learnsets()
    if learnsets:
        return ResponseModel(learnsets, "Compétences récupérées avec succès.")
    return ResponseModel(learnsets, "Aucune compétence trouvée.")

@router.put("/{id}")
async def update_learnset_data(id: str, req: LearnsetUpdate = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_learnset = await update_learnset(id, req)
    if updated_learnset:
        return ResponseModel(
            "Compétence avec ID: {} mise à jour avec succès.".format(id),
            "Compétence mise à jour avec succès."
        )
    return ResponseModel(
        "Impossible de mettre à jour la compétence avec ID: {}".format(id),
        "Mise à jour de la compétence impossible."
    )

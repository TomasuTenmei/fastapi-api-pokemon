import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Learnset(BaseModel):
    
    id: str = Field(default_factory=uuid.uuid4, alias="id")
    name: str = Field(...)
    description: str = Field(...)
    power: int = Field(...)
    precision: int = Field(...)
    pp: int = Field(...)
    type: str = Field(...)

    class Config:
        
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "id": "653a554236887f3385e5b733",
                "name": "Abîme",
                "description": "Peut mettre K.O. en un coup. Sans effet sur les Pokémon Vol.",
                "power": 0,
                "precision": 30,
                "pp": 5,
                "type": "Normal"
            }
        }

class LearnsetUpdate(BaseModel):
    
    name: str
    description: Optional[str]
    power: Optional[int]
    precision: Optional[int]
    pp: Optional[int]
    type: Optional[str]
    
    class Config:
        
        json_schema_extra = {
            "example": {
                "name": "Abîme",
                "description": "Peut mettre K.O. en un coup. Sans effet sur les Pokémon Vol.",
                "power": 0,
                "precision": 30,
                "pp": 5,
                "type": "Normal"
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

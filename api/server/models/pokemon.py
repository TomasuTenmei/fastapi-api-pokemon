import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Statistic(BaseModel):
    
    hp: int = Field(..., alias="HP")
    attack: int = Field(..., alias="Attack")
    defense: int = Field(..., alias="Defense")
    spAttack: int = Field(..., alias="Sp. Attack")
    spDefense: int = Field(..., alias="Sp. Defense")
    speed: int = Field(..., alias="Speed")

class Pokemon(BaseModel):
    
    id: str = Field(default_factory=uuid.uuid4, alias="id")
    number: int = Field(...)
    name: str = Field(...)
    size: str = Field(...)
    weight: str = Field(...)
    statistic: Statistic = Field(...)
    type: list = Field(...)
    learnset: list = Field(...)
    
    class Config:
        
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "id": "653a54a936887f3385e5b086",
                "id": 1,
                "name": "Bulbizarre",
                "size": "0.7 m",
                "weight": "6.9 kg",
                "statistic": {
                    "hp": 45,
                    "attack": 49,
                    "defense": 49,
                    "spAttack": 65,
                    "spDefense": 65,
                    "speed": 45
                },
                "type": [
                    "Grass",
                    "Poison"
                ],
                "learnset": [
                    "Charge",
                    "Rugissement",
                    "Fouet Lianes",
                    "Croissance",
                    "Vampigraine",
                    "Tranch'Herbe",
                    "Poudre Dodo",
                    "Poudre Toxik",
                    "Canon Graine",
                    "Bélier",
                    "Doux Parfum",
                    "Synthèse",
                    "Soucigraine",
                    "Damoclès",
                    "Lance-Soleil"
                ]
            }
        }

class PokemonUpdate(BaseModel):
        
    number: int
    name: str
    size: Optional[str]
    weight: Optional[str]
    statistic: Optional[Statistic]
    type: Optional[list]
    learnset: Optional[list]
    
    class Config:
        
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Bulbizarre",
                "size": "0.7 m",
                "weight": "6.9 kg",
                "statistic": {
                    "hp": 45,
                    "attack": 49,
                    "defense": 49,
                    "spAttack": 65,
                    "spDefense": 65,
                    "speed": 45
                },
                "type": [
                    "Grass",
                    "Poison"
                ],
                "learnset": [
                    "Charge",
                    "Rugissement",
                    "Fouet Lianes",
                    "Croissance",
                    "Vampigraine",
                    "Tranch'Herbe",
                    "Poudre Dodo",
                    "Poudre Toxik",
                    "Canon Graine",
                    "Bélier",
                    "Doux Parfum",
                    "Synthèse",
                    "Soucigraine",
                    "Damoclès",
                    "Lance-Soleil"
                ]
            }
        }
        
def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message
    }
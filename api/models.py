import uuid
from typing import Optional
from pydantic import BaseModel, Field

"""
╔════════════════════╗
║ Collection Pokemon ║
╚════════════════════╝
"""

class Statistic(BaseModel):
    
    hp: int = Field(..., alias="HP")
    attack: int = Field(..., alias="Attack")
    defense: int = Field(..., alias="Defense")
    spAttack: int = Field(..., alias="Sp. Attack")
    spDefense: int = Field(..., alias="Sp. Defense")
    speed: int = Field(..., alias="Speed")

class Pokemon(BaseModel):
    
    _id: str = Field(default_factory=uuid.uuid4, alias="_id")
    number: int = Field(...)
    name: str = Field(...)
    size: str = Field(...)
    weight: str = Field(...)
    statistic: Statistic = Field(...)
    type: list = Field(...)
    learnset: list = Field(...)
    
    class Config:
        
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "653a54a936887f3385e5b086",
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
        
        schema_extra = {
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
        
        
"""   
╔═════════════════╗
║ Collection Type ║
╚═════════════════╝
"""

class Types(BaseModel):
    
    _id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)

    class Config:
        
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "653a556336887f3385e5b998",
                "name": "Normal"
            }
        }

class TypesUpdate(BaseModel):
    
    name : str
    
    class Config:
        
        schema_extra = {
            "example": {
                "name": "Normal"
            }
        }
        

"""   
╔═════════════════════╗
║ Collection learnset ║
╚═════════════════════╝
"""

class Learnset(BaseModel):
    
    _id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    description: str = Field(...)
    power: int = Field(...)
    precision: int = Field(...)
    pp: int = Field(...)
    type: str = Field(...)

    class Config:
        
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "653a554236887f3385e5b733",
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
        
        schema_extra = {
            "example": {
                "name": "Abîme",
                "description": "Peut mettre K.O. en un coup. Sans effet sur les Pokémon Vol.",
                "power": 0,
                "precision": 30,
                "pp": 5,
                "type": "Normal"
            }
        }

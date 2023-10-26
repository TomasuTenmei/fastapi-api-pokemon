import uuid
from typing import Optional
from pydantic import BaseModel, Field

"""
╔════════════════════╗
║ Collection Pokemon ║
╚════════════════════╝
"""

class Name(BaseModel):
    
    english: str = Field(..., alias="english")
    japanese: str = Field(..., alias="japanese")
    chinese: str = Field(..., alias="chinese")
    french: str = Field(..., alias="french")

class BaseStats(BaseModel):
    
    hp: int = Field(..., alias="HP")
    attack: int = Field(..., alias="Attack")
    defense: int = Field(..., alias="Defense")
    spAttack: int = Field(..., alias="Sp. Attack")
    spDefense: int = Field(..., alias="Sp. Defense")
    speed: int = Field(..., alias="Speed")

class Pokemon(BaseModel):
    
    _id: str = Field(default_factory=uuid.uuid4, alias="_id")
    id: int = Field(...)
    name: Name
    type: list = Field(...)
    base: BaseStats
    
    class Config:
        
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "653a54a936887f3385e5b086",
                "id": 1,
                "name": {
                    "english": "Bulbasaur",
                    "japanese": "フシギダネ",
                    "chinese": "妙蛙种子",
                    "french": "Bulbizarre"
                },
                "type": [
                    "Grass",
                    "Poison"
                ],
                "base": {
                    "hp": 45,
                    "attack": 49,
                    "defense": 49,
                    "spAttack": 65,
                    "spDefense": 65,
                    "speed": 45
                }
            }
        }

class PokemonUpdate(BaseModel):
        
    id: Optional[int]
    name: Optional[Name]
    type: Optional[list]
    base: Optional[BaseStats]
    
    class Config:
        
        schema_extra = {
            "example": {
                "id": 1,
                "name": {
                    "english": "Bulbasaur",
                    "japanese": "フシギダネ",
                    "chinese": "妙蛙种子",
                    "french": "Bulbizarre"
                },
                "type": [
                    "Grass",
                    "Poison"
                ],
                "base": {
                    "hp": 45,
                    "attack": 49,
                    "defense": 49,
                    "spAttack": 65,
                    "spDefense": 65,
                    "speed": 45
                }
            }
        }
        
        
"""   
╔══════════════════╗
║ Collection Types ║
╚══════════════════╝
"""

class Types(BaseModel):
    
    _id: str = Field(default_factory=uuid.uuid4, alias="_id")
    english: str = Field(..., alias="english")
    chinese: str = Field(..., alias="chinese")
    japanese: str = Field(..., alias="japanese")

    class Config:
        
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "653a556336887f3385e5b998",
                "english": "Normal",
                "chinese": "一般",
                "japanese": "ノーマル"
            }
        }

class TypesUpdate(BaseModel):
    
    english: Optional[str]
    chinese: Optional[str]
    japanese: Optional[str]
    
    class Config:
        
        schema_extra = {
            "example": {
                "english": "Normal",
                "chinese": "一般",
                "japanese": "ノーマル"
            }
        }
        

"""   
╔══════════════════╗
║ Collection Moves ║
╚══════════════════╝
"""

class Moves(BaseModel):
    
    _id: str = Field(default_factory=uuid.uuid4, alias="_id")
    accuracy: int = Field(..., alias="accuracy")
    category: str = Field(..., alias="category")
    cname: str = Field(..., alias="cname")
    ename: str = Field(..., alias="ename")
    id: int = Field(..., alias="id")
    jname: str = Field(..., alias="jname")
    power: int = Field(..., alias="power")
    pp: int = Field(..., alias="pp")
    type: str = Field(..., alias="type")

    class Config:
        
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "653a554236887f3385e5b733",
                "accuracy": 100,
                "category": "物理",
                "cname": "物理",
                "ename": "Pound",
                "id": 1,
                "jname": "はたく",
                "power": 40,
                "pp": 35,
                "type": "Normal"
            }
        }

class MovesUpdate(BaseModel):
    
    accuracy: Optional[int]
    category: Optional[str]
    cname: Optional[str]
    ename: Optional[str]
    id: Optional[int]
    jname: Optional[str]
    power: Optional[int]
    pp: Optional[int]
    type: Optional[str]
    
    class Config:
        
        schema_extra = {
            "example": {
                "accuracy": 100,
                "category": "物理",
                "cname": "物理",
                "ename": "Pound",
                "id": 1,
                "jname": "はたく",
                "power": 40,
                "pp": 35,
                "type": "Normal"
            }
        }
    

"""   
╔══════════════════╗
║ Collection Items ║
╚══════════════════╝
"""

class Items(BaseModel):
    
    _id: str = Field(default_factory=uuid.uuid4, alias="_id")
    id: int = Field(..., alias="id")
    name: Name
    
    class Config:
        
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "653a554236887f3385e5b733",
                "id": 1,
                "name": {
                    "english": "Master Ball",
                    "japanese": "マスターボール",
                    "chinese": "大师球",
                    "french": "Master Ball"
                }
            }
        }
        
class ItemsUpdate(BaseModel):
    
    id: Optional[int]
    name: Optional[Name]
    
    class Config:
        
        schema_extra = {
            "example": {
                "id": 1,
                "name": {
                    "english": "Master Ball",
                    "japanese": "マスターボール",
                    "chinese": "大师球",
                    "french": "Master Ball"
                }
            }
        }

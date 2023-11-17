import uuid
from typing import Optional
from pydantic import BaseModel, Field

class PkTypes(BaseModel):
    
    id: str = Field(default_factory=uuid.uuid4, alias="id")
    name: str = Field(...)

    class Config:
        
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "id": "653a556336887f3385e5b998",
                "name": "Normal"
            }
        }

class PkTypesUpdate(BaseModel):
    
    name : str
    
    class Config:
        
        json_schema_extra = {
            "example": {
                "name": "Normal"
            }
        }
      
def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

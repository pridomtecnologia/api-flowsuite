from typing import List
from pydantic import BaseModel

class ListPermissionSchema(BaseModel):
    id_permission: int
    permission: str
    
    class Config:
        orm_mode = True

class RegisterPermissionSchema(BaseModel):
    permission: str
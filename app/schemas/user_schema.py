from pydantic import BaseModel, Field, validator
from typing import List

class CreateUserSchemas(BaseModel):
    name: str = Field(..., example="John Doe")
    email: str = Field(..., example="john.doe@example.com")
    password: str = Field(..., example="strongpassword")
    permissions: List[int] = Field(..., example=[1, 2, 3])
    role_id: int = Field(..., example=1)

    @validator('name')
    def name_must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError('Invalid Name')
        return value
    
    @validator('email')
    def email_must_be_valid(cls, value):
        if '@' not in value or '.' not in value.split('@')[-1]:
            raise ValueError('Invalid email')
        return value
    
class UserLoginSchemas(BaseModel):
    email: str = Field(..., example="john.doe@example.com")
    password: str = Field(..., example="strongpassword")
    
class AtualizarUserSchemas(BaseModel):
    name: str
    email: str
    # permissions: List[int]
    # role_id: int
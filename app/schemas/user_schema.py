import re
from pydantic import BaseModel

class UserSchemas(BaseModel):
    name: str
    email: str
    password: str
    
class UserLoginSchemas(BaseModel):
    email: str
    password: str
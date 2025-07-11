import re
from pydantic import BaseModel, validator

class UserSchemas(BaseModel):
    name: str
    email: str
    password: str

    @validator('name')
    def validate_username(cls, value):
        if not re.match('^([a-z]|[0-9]|@)+$', value):
            raise ValueError('Username format invalid')
        return value
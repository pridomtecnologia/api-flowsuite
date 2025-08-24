from pydantic import BaseModel
from typing import List

class TagSchema(BaseModel):
    id_tag: int
    tag: str
    
class TagListSchema(BaseModel):
    tags: List[TagSchema]
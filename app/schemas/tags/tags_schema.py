from pydantic import BaseModel

class TagSchema(BaseModel):
    id_tag: int
    tag: str
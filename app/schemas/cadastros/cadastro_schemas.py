from typing import List
from pydantic import BaseModel

class EnderecoSchema(BaseModel):
    address: str
    bairro: str
    numero: str
    estado: str
    cidade: str
    cep: str
    complemento: str | None = None

class RegisterSchema(BaseModel):
    id_user: int
    tag_id: int
    razao_social: str
    nome_fantasia: str
    documento: str
    email: str
    telefone: str
    responsavel_contato: str
    observacao: str
    address: List[EnderecoSchema]

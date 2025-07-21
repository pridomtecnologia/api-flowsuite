from typing import List
from pydantic import BaseModel

class EnderecoCustomerSchema(BaseModel):
    address: str
    bairro: str
    numero: str
    estado: str
    cidade: str
    cep: str
    complemento: str | None = None

class RegisterCustomerSchema(BaseModel):
    id_user: int
    razao_social: str
    nome_fantasia: str
    cnpj: str
    email: str
    telefone: str
    responsavel_contato: str
    observacao: str
    address: List[EnderecoCustomerSchema]

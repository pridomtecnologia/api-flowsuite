from pydantic import BaseModel

class CustomerSchemas(BaseModel):
    razao_social: str
    nome_fantasia: str
    cnpj: str
    email: str
    telefone: str
    responsavel_contato: str
    observacao: str
from fastapi import FastAPI
from app.api.usuario import usuario_api
from app.api.cadastro import cadastro_api
from app.api.orcamento import orcamento_api
from app.api.permissions import permission_api

app = FastAPI()

app.include_router(usuario_api.router)
app.include_router(cadastro_api.router)
app.include_router(orcamento_api.router)
app.include_router(permission_api.router)
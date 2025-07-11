from fastapi import FastAPI
from app.api.usuario import usuario_api

app = FastAPI()

app.include_router(usuario_api.router)

# app.include_router(autenticacao.test_router)
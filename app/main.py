from fastapi import FastAPI
from app.api import autenticacao

app = FastAPI()

app.include_router(autenticacao.router)

app.include_router(autenticacao.test_router)
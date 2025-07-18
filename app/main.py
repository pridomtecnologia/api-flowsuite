from fastapi import FastAPI
from app.api.usuario import usuario_api
from app.api.customer import customer_api

app = FastAPI()

app.include_router(usuario_api.router)
app.include_router(customer_api.router)
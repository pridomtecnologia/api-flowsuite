from fastapi import FastAPI
from app.api.usuario import usuario_api
from app.api.cadastro import cadastro_api
from app.api.orcamento import orcamento_api
from app.api.permissions import permission_api
from app.api.tags import tags_api
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuario_api.router)
app.include_router(cadastro_api.router)
app.include_router(orcamento_api.router)
app.include_router(permission_api.router)
app.include_router(tags_api.router)
from fastapi import APIRouter, Depends
from app.drivers.database import get_db_session, token_verifier
from sqlalchemy.orm import Session
from app.schemas.orcamento.orcamento_schema import CriarOrcamentoSchema

router = APIRouter(prefix="/orcamento", tags=["orcamento"], dependencies=[Depends(token_verifier)])

@router.post("/create")
def create(orcamento: CriarOrcamentoSchema, db_session: Session = Depends(get_db_session)):
    return {"create": "Criar Orçamento"}

@router.get("/listar")
def list(db_session: Session = Depends(get_db_session)):
    return {"listar": "Listar Orçamento"}
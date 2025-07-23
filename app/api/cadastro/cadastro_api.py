from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.drivers.database import get_db_session, token_verifier
from app.schemas.cadastros.cadastro_schemas import RegisterSchema
from app.controllers.cadastro.cadastro_controller import CadastroController

router = APIRouter(prefix='/cadastro', tags=['cadastro'], dependencies=[Depends(token_verifier)])

@router.post('/create', summary='Cadastrar cliente, fornecedor, funcionário, artista no sistema')
def create(cadastro: RegisterSchema, db_session: Session = Depends(get_db_session)):
 
    try:
        return CadastroController(db_session=db_session).incluir_cadastro(cadastro=cadastro)
    except Exception as e:
        raise e

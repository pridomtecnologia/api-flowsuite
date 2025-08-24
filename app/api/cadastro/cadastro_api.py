from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.drivers.database import get_db_session, token_verifier
from app.schemas.cadastros.cadastro_schemas import RegisterSchema, UpdateCadastroSchema
from app.controllers.cadastro.cadastro_controller import CadastroController

router = APIRouter(prefix='/cadastro', tags=['cadastro'], dependencies=[Depends(token_verifier)])

@router.post('/create', summary='Cadastrar cliente, fornecedor, funcionário, artista no sistema')
def create(cadastro: RegisterSchema, db_session: Session = Depends(get_db_session)):
 
    try:
        return CadastroController(db_session=db_session).incluir_cadastro(cadastro=cadastro)
    except Exception as e:
        raise e

@router.get('/list', summary='Listar todos os cadastros no sistema')
def listar(db_session: Session = Depends(get_db_session)):
    try:
        return CadastroController(db_session=db_session).listar_cadastro()
    except Exception as e:
        raise e

@router.put('/atualizar/{id_cadastro}', dependencies=[Depends(token_verifier)], summary='Atualizar cadastro no sistema')
def atualizar(id_cadastro: int, cadastro: UpdateCadastroSchema, db_session: Session = Depends(get_db_session)):
    return CadastroController(db_session=db_session).atualizar_cadastro(id_cadastro=id_cadastro, cadastro=cadastro)

@router.delete('/delete/{id_cadastro}', dependencies=[Depends(token_verifier)], summary='Deletar cadastro no sistema')
def delete(id_cadastro: int, db_session: Session = Depends(get_db_session)):
    return CadastroController(db_session=db_session).deletar_cadastro(id_cadastro=id_cadastro)
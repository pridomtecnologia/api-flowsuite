from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.drivers.database import get_db_session, token_verifier
from app.schemas.tags.tags_schema import TagSchema
from app.controllers.tags.tag_controller import TagController

router = APIRouter(prefix='/tag', tags=['tags'], dependencies=[Depends(token_verifier)])

@router.post('/create', summary='Cadastrar tags')
def create(cadastro_tag: TagSchema, db_session: Session = Depends(get_db_session)):
 
    try:
        return TagController(db_session=db_session).incluir_tag(cadastro_tag=cadastro_tag)
    except Exception as e:
        raise e
    
@router.get('/list', summary='Listar Tags')
def listar(db_session: Session = Depends(get_db_session)):
    
    try:
        return TagController(db_session=db_session).listar_tag()
    except Exception as e:
        raise e
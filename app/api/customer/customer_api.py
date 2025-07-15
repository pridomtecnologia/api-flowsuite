from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.drivers.database import get_db_session, token_verifier

router = APIRouter(prefix='/customer', tags=['usuario'], dependencies=[Depends(token_verifier)])

@router.post('/register', summary='Cadastrar cliente no sistema')
def register(db_session: Session = Depends(get_db_session)):
    
    return {'test': 'autenticado'}

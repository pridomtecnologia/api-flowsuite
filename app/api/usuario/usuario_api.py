from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.drivers.database import get_db_session, token_verifier
from app.controllers.usuario.usuario_controller import UsuarioController
from app.schemas.user_schema import CreateUserSchemas, UserLoginSchemas, AtualizarUserSchemas

router = APIRouter(prefix='/user', tags=['usuario'])

@router.post('/register', dependencies=[Depends(token_verifier)], summary='Cadastrar usuário no sistema')
def register(user: CreateUserSchemas, db_session: Session = Depends(get_db_session)):
    
    return UsuarioController(db_session=db_session).user_register(user=user)
    
@router.post('/login', summary='Realizar autenticação do usuário no sistema')
def login(request_form_user: OAuth2PasswordRequestForm = Depends(), db_session: Session = Depends(get_db_session)):

    user = UserLoginSchemas(
        email=request_form_user.username,
        password=request_form_user.password
    )
    
    return UsuarioController(db_session=db_session).user_login(user=user)

@router.get('/list', dependencies=[Depends(token_verifier)], summary='Listar usuários cadastrados no sistema')
def list_users(db_session: Session = Depends(get_db_session)):
    return UsuarioController(db_session=db_session).list_users()

@router.put('/atualizar/{id_user}', dependencies=[Depends(token_verifier)], summary='Atualizar usuário no sistema')
def atualizar_user(id_user: int, user: AtualizarUserSchemas, db_session: Session = Depends(get_db_session)):
    return UsuarioController(db_session=db_session).user_update(id_user=id_user, user=user)

@router.delete('/delete/{id_user}', dependencies=[Depends(token_verifier)], summary='Deletar usuário no sistema')
def delete_user(id_user: int, db_session: Session = Depends(get_db_session)):
    return UsuarioController(db_session=db_session).user_delete(id_user=id_user)
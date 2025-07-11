from fastapi import status, HTTPException
from fastapi.responses import JSONResponse
from app.use_cases.usuario.user_use_cases import UserUseCases

class UsuarioController:
    
    def __init__(self, db_session):
        self.db_session = db_session

    def user_register(self, user):
        
        if not user.name or not user.email or not user.password:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail={'message': 'Obrigatório preencher todas informações'},
            )
        
        try:
            
            use_case = UserUseCases(db_session=self.db_session).user_register(user=user)
            
            return JSONResponse(
                content={'message': 'Usuário criado com sucesso'},
                status_code=status.HTTP_201_CREATED
            )
            
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={'message': 'Erro ao cadastrar usuário'}
            )
            
    def user_login(self, user):
        
        if not user.email or not user.password:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail={'message': 'E-mail ou senha inválida'},
            )
        
        try:
            
            use_case_login = UserUseCases(db_session=self.db_session).user_login(user=user)
            
            return JSONResponse(
                content=use_case_login,
                status_code=status.HTTP_200_OK
            )
            
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail={'message': 'Erro ao realizar autenticação'}
            )
from fastapi import status, HTTPException
from fastapi.responses import JSONResponse
from app.use_cases.cadastros.cadastro_use_cases import CadastroUseCases

class CadastroController:
    
    def __init__(self, db_session):
        self.db_session = db_session
        self.customer_use_case = CadastroUseCases(self.db_session)
        
    def incluir_cadastro(self, cadastro):
        
        try:
            self.customer_use_case.incluir_cadastro(cadastro=cadastro)

            return JSONResponse(content={'message':'Cadastrado com sucesso'}, status_code=status.HTTP_201_CREATED)
        
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Erro no cadastro!")
    
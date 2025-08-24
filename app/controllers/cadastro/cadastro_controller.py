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
            import traceback
            traceback.print_exc()
            self.db_session.rollback()
            raise HTTPException(status_code=400, detail=str(e))

            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Erro no cadastro!")
        
    def listar_cadastro(self):
        
        try:
            cadastros = self.customer_use_case.listar_cadastro()
            return JSONResponse(content=cadastros, status_code=status.HTTP_200_OK)
        
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Erro ao listar cadastros!")

    def atualizar_cadastro(self, id_cadastro: int, cadastro):
        try:
            self.customer_use_case.atualizar_cadastro(id_cadastro=id_cadastro, cadastro=cadastro)
            return JSONResponse(content={'message':'Atualizado com sucesso'}, status_code=status.HTTP_200_OK)

        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Erro ao atualizar cadastro!")

    def deletar_cadastro(self, id_cadastro: int):
        try:
            self.customer_use_case.deletar_cadastro(id_cadastro=id_cadastro)
            return JSONResponse(content={'message':'Deletado com sucesso'}, status_code=status.HTTP_200_OK)

        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Erro ao deletar cadastro!")

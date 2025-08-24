from fastapi import status, HTTPException
from fastapi.responses import JSONResponse
from app.gateways.tags.tag_gateway import TagGateway

class TagController:
    
    def __init__(self, db_session):
        self.db_session = db_session
        self.tag_gateway = TagGateway(self.db_session)
        
    def incluir_tag(self, cadastro_tag):
        
        try:
            self.tag_gateway.incluir_tag(cadastro_tag=cadastro_tag)
            
            return JSONResponse(content={'message':'Tag cadastrada com sucesso'}, status_code=status.HTTP_201_CREATED)
        
        except Exception as e:
            import traceback
            traceback.print_exc()
            self.db_session.rollback()
            raise HTTPException(status_code=400, detail=str(e))

    def listar_tag(self):
        
        try:
            
            listar_tags = self.tag_gateway.listar_tag()
            
            return JSONResponse(content=listar_tags, status_code=status.HTTP_200_OK)
        
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Erro ao listar as tags!")
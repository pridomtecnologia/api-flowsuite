from fastapi import status, HTTPException
from fastapi.responses import JSONResponse
from app.gateways.permissions.permisson_gateway import PermissionGateway

class PermissionsController:
    
    def __init__(self, db_session):
        self.db_session = db_session
        self.permission_use_case = PermissionGateway(db_session=self.db_session)

    def incluir_permission(self, permission):
        
        try:
            self.permission_use_case.incluir_permission(permission=permission)
            
            return JSONResponse(content={'message':'Permissão cadastrada com sucesso'}, status_code=status.HTTP_201_CREATED)

        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Erro ao cadastrar permissão!")
        
    def listar_permission(self):
        
        try:
            permission = self.permission_use_case.listar_permission()
            
            return JSONResponse(content=permission, status_code=status.HTTP_200_OK)
        
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Erro ao listar permissões!")

from app.entidades.permissions.permissions_entities import PermissionEntities
from app.schemas.permissions.permissions_schemas import RegisterPermissionSchema, ListPermissionSchema
from app.models.permission.permission_model import PermissionModel
from typing import List

class PermissionGateway(PermissionEntities):

    def __init__(self, db_session):
        self.db_session = db_session

    def incluir_permission(self, permission: RegisterPermissionSchema):

        try:
            
            permission_model = PermissionModel(
                permission=permission.permission
            )
            
            self.db_session.add(permission_model)
            self.db_session.commit()
            
            return True
            
        except Exception as e:
            raise False
    
    def listar_permission(self) -> List[ListPermissionSchema]:
        
        try:
            
            permissions = self.db_session.query(PermissionModel).all()
            
            permissions_array = []
            
            for p in permissions:
                permissions_array.append({
                    "id_permission": p.id_permission,
                    "permission": p.permission
                })

            return permissions_array

        except Exception as e:
            raise False
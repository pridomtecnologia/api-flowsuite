from abc import ABC, abstractmethod
from app.schemas.permissions.permissions_schemas import RegisterPermissionSchema, ListPermissionSchema
from typing import List

class PermissionEntities(ABC):
    
    @abstractmethod
    def incluir_permission(self, permission: RegisterPermissionSchema): pass
    
    @abstractmethod
    def listar_permission(self) -> List[ListPermissionSchema]: pass
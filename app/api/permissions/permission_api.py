from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controllers.permissions.permissions_controller import PermissionsController
from app.drivers.database import get_db_session, token_verifier
from app.schemas.permissions.permissions_schemas import RegisterPermissionSchema

router = APIRouter(prefix='/permissions', tags=['permissions'], dependencies=[Depends(token_verifier)])

@router.post('/create', summary='Cadastrar permissão')
def create(permission: RegisterPermissionSchema, db_session: Session = Depends(get_db_session)):
    """Cadastrar permissão"""
 
    try:
        return PermissionsController(db_session=db_session).incluir_permission(permission=permission)
    except Exception as e:
        raise e
    
@router.get('/listar', summary='listar permissões')
def list(db_session: Session = Depends(get_db_session)):
    """Listar permissões"""
    try:
        return PermissionsController(db_session=db_session).listar_permission()
    except Exception as e:
        raise e
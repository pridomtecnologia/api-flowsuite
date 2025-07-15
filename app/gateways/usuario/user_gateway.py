from fastapi import status
from fastapi.exceptions import HTTPException
from app.models.usuario.usuario_model import UsuarioModel
from app.models.role.role_model import RoleModel
from app.models.permission.permission_model import PermissionModel
from app.models.user_role.user_role_model import UserRoleModel
from app.models.role_permission.role_permission_model import RolePermissionModel
from app.models.permission.permission_model import PermissionModel
from app.entidades.usuario.usuario_entidade import UsuarioEntidade
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt, JWTError
from decouple import config
from sqlalchemy import func

SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')

crypt_context = CryptContext(schemes=['sha256_crypt'])

class UserGateway(UsuarioEntidade):
    
    def __init__(self, db_session):
        self.db_session = db_session
        
    def user_register(self, user): 
        
        try:
            user_model = UsuarioModel(
                name=user.name,
                email=user.email,
                password=crypt_context.hash(user.password)
            )
            
            self.db_session.add(user_model)
            self.db_session.commit()
        except Exception as e:
            raise False
    
    def user_login(self, user, expires_in): 
        
        try:
            user_on_db = self.db_session.query(UsuarioModel).filter_by(email=user.email).first()
            
            if user_on_db is None:
                raise False
            
            if not crypt_context.verify(user.password, user_on_db.password):
                raise False
            
            exp = datetime.utcnow() + timedelta(minutes=expires_in)

            payload = {
                'sub': user.email,
                'exp': exp
            }
            
            permission_usuario = self.get_user_permissions(user_id=user_on_db.id_user)

            access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

            return {
                'id_user': user_on_db.id_user,
                'name': user_on_db.name,
                'email': user_on_db.email,
                'access_token': access_token,
                'exp': exp.isoformat(),
                'permissions': permission_usuario
            }
        except Exception as e:
            raise False
    
    def get_user_permissions(self, user_id):  
        
        query = (
            self.db_session.query(
                UsuarioModel.id_user,
                UsuarioModel.name,
                RoleModel.role,
                func.STRING_AGG(PermissionModel.permission, ', ').label("permissions")
            )
            .join(UserRoleModel, UserRoleModel.user_id == UsuarioModel.id_user)
            .join(RoleModel, RoleModel.id_role == UserRoleModel.role_id)
            .join(RolePermissionModel, RolePermissionModel.role_id == RoleModel.id_role)
            .join(PermissionModel, PermissionModel.id_permission == RolePermissionModel.permission_id)
            .filter(UsuarioModel.id_user == user_id)
            .group_by(UsuarioModel.id_user, UsuarioModel.name, RoleModel.role)
        )

        result = query.first()

        if not result:
            raise False

        return {
            "role":result.role,
            "permissions":result.permissions
        }
        
    def verify_token(self, access_token):
        
        try:
            data = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid access token'
            )
        
        user_on_db = self.db_session.query(UsuarioModel).filter_by(email=data['sub']).first()

        if user_on_db is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid access token'
            )
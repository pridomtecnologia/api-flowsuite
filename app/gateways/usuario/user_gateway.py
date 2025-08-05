from sqlite3 import IntegrityError
from fastapi import status
from fastapi.exceptions import HTTPException
from app.models.usuario.usuario_model import UsuarioModel
from app.models.role.role_model import RoleModel
from app.models.permission.permission_model import PermissionModel
from app.models.user_role.user_role_model import UserRoleModel
from app.models.role_permission.role_permission_model import UserPermissionModel
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
            
            id_user = user_model.id_user

            user_role_model = UserRoleModel(
                user_id=id_user,
                role_id=user.role_id
            )

            self.db_session.add(user_role_model)
            self.db_session.commit()

            for user_permission in user.permissions:
                print(user_permission)
                
                user_permission_model = UserPermissionModel(
                    user_id=id_user,
                    permission_id=user_permission
                )
                
                self.db_session.add(user_permission_model)
                self.db_session.commit()

            return True
        
        except IntegrityError:
            self.db_session.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='E-mail já cadastrado'
            )
        except Exception as e:
            raise False
        
    def list_users(self):
        
        try:
            consult_list_users =  self.db_session.query(UsuarioModel).all()
            
            list_users = []
            for consult_list_user in consult_list_users:
                list_users.append({
                                   'id_user': consult_list_user.id_user,
                                   'name': consult_list_user.name,
                                   'email': consult_list_user.email
                                })

            return list_users

        except Exception as e:
            raise False
  
    def user_update(self, id_user, user): 
        
        try:
            user_on_db = self.db_session.query(UsuarioModel).filter_by(id_user=id_user).first()
            
            if not user_on_db:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='Usuário não encontrado'
                )
            
            user_on_db.name = user.name
            user_on_db.email = user.email
            
            self.db_session.commit()
            
            return {
                'name': user_on_db.name,
                'email': user_on_db.email
            }
        
        except Exception as e:
            raise False
        
    def user_delete(self, id_user):
        
        try:
            user_on_db = self.db_session.query(UsuarioModel).filter_by(id_user=id_user).first()
            
            if not user_on_db:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='Usuário não encontrado'
                )
            
            self.db_session.delete(user_on_db)
            self.db_session.commit()
            
            return True
        
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
            .join(UserPermissionModel, UserPermissionModel.user_id == UsuarioModel.id_user)
            .join(PermissionModel, PermissionModel.id_permission == UserPermissionModel.permission_id)
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
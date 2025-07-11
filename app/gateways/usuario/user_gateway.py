from app.models.usuario.usuario_model import UsuarioModel
from app.entidades.usuario.usuario_entidade import UsuarioEntidade
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt, JWTError
from decouple import config

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

            access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

            return {
                'access_token': access_token,
                'exp': exp.isoformat()
            }
        except Exception as e:
            raise False
    
from app.models.usuario.usuario_model import UsuarioModel
from app.entidades.usuario.usuario_entidade import UsuarioEntidade
from passlib.context import CryptContext

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
    
    def user_login(self, user, expires_in): pass
    
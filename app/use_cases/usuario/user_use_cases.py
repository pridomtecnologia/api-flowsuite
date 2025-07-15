from sqlalchemy.exc import IntegrityError

from app.gateways.usuario.user_gateway import UserGateway
from app.entidades.usuario.usuario_entidade import UsuarioEntidade

class UserUseCases(UsuarioEntidade):
    
    def __init__(self, db_session):
        self.db_session = db_session

    def user_register(self, user):

        try:
            UserGateway(db_session=self.db_session).user_register(user)
            
            return True
        except IntegrityError:
            raise False

    def user_login(self, user, expires_in: int = 30):
        try:
            return UserGateway(db_session=self.db_session).user_login(user=user, expires_in=expires_in)
        except IntegrityError:
            raise False
        except Exception as e:
            raise False
        
from sqlalchemy.exc import IntegrityError

from app.gateways.cadastro.cadastro_gateway import CadastroGateway
from app.gateways.addresses.address_gateway import AddressGateway
from app.entidades.cadastros.cadastro_entities import CadastroEntities

class CadastroUseCases(CadastroEntities):
    
    def __init__(self, db_session):
        self.db_session = db_session
        self.cadastro_gateway = CadastroGateway(self.db_session)
        self.address_gateway = AddressGateway(self.db_session)

    def incluir_cadastro(self, cadastro): 
        
        try:
            
            id_cadastro = self.cadastro_gateway.incluir_cadastro(cadastro=cadastro)

            return self.address_gateway.create_address(address=cadastro.address[0], owner_id=id_cadastro)
        
        except IntegrityError:
            raise False
        except Exception as e:
            raise False
        
    def listar_cadastro(self): 
        try:
            return self.cadastro_gateway.listar_cadastro()
        except Exception as e:
            raise False
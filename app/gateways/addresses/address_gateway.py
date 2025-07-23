from app.entidades.addresses.address_entities import AddressEntities
from app.models.address.address_model import AddressModel

class AddressGateway(AddressEntities):
    
    def __init__(self, db_session):
        self.db_session = db_session
        
    def create_address(self, address, owner_id):
        try:
            
            adrress_model = AddressModel(
                address=address.address,
                bairro=address.bairro,
                numero=address.numero,                
                estado=address.estado,
                cidade=address.cidade,
                cep=address.cep,
                complemento=address.complemento,
                owner_id=owner_id,
            )
            
            self.db_session.add(adrress_model)
            self.db_session.commit()
            
            return True
            
        except Exception as e:
            raise False
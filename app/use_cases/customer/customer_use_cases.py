from sqlalchemy.exc import IntegrityError

from app.gateways.customer.customer_gateway import CustomerGateway
from app.gateways.addresses.address_gateway import AddressGateway
from app.entidades.customers.customer_entities import CustomerEntities

class CustomerUseCases(CustomerEntities):
    
    def __init__(self, db_session):
        self.db_session = db_session
        self.customer_gateway = CustomerGateway(self.db_session)
        self.address_gateway = AddressGateway(self.db_session)

    def create_customer(self, customer): 
        
        try:
            if not customer.razao_social or not customer.cnpj:
                return False
            
            id_customer = self.customer_gateway.create_customer(customer=customer)

            return self.address_gateway.create_address(address=customer.address[0], owner_type='customer', owner_id=id_customer)
        
        except IntegrityError:
            raise False
        except Exception as e:
            raise False
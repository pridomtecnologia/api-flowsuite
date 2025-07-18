from app.entidades.customers.customer_entities import CustomerEntities
from app.schemas.customer.customer_schemas import RegisterCustomerSchemas
from app.models.customer.customer_model import CustomerModel

class CustomerGateway(CustomerEntities):
    
    def __init__(self, db_session):
        self.db_session = db_session
        
    def create_customer(self, customer: RegisterCustomerSchemas):
        
        try:
            customer_model = CustomerModel(
                razao_social=customer.razao_social,
                nome_fantasia=customer.nome_fantasia,
                cnpj=customer.cnpj,
                email=customer.email,
                telefone=customer.telefone,
                responsavel_contato=customer.responsavel_contato,
                observacao=customer.observacao
            )
            
            self.db_session.add(customer_model)
            self.db_session.commit()
            
        except Exception as e:
            raise False
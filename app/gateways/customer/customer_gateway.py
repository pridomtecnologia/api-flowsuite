from app.entidades.customers.customer_entities import CustomerEntities
from app.schemas.customer.customer_schemas import RegisterCustomerSchema
from app.models.customer.customer_model import CustomerModel
from app.models.user_customer.user_customer_model import UserCustomerModel

class CustomerGateway(CustomerEntities):
    
    def __init__(self, db_session):
        self.db_session = db_session
        
    def create_customer(self, customer: RegisterCustomerSchema):
        
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
            
            id_customer = customer_model.id_customer
            
            user_customer_model = UserCustomerModel(
                user_id=customer.id_user,
                customer_id=id_customer
            )
            
            self.db_session.add(user_customer_model)
            self.db_session.commit()
            
            return id_customer
            
        except Exception as e:
            raise False
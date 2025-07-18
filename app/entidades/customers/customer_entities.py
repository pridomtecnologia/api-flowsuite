from abc import ABC, abstractmethod
from app.schemas.customer.customer_schemas import RegisterCustomerSchemas

class CustomerEntities(ABC):
    
    @abstractmethod
    def create_customer(self, customer: RegisterCustomerSchemas): pass
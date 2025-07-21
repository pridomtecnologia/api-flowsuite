from fastapi import status, HTTPException
from fastapi.responses import JSONResponse
from app.use_cases.customer.customer_use_cases import CustomerUseCases

class CustomerController:
    
    def __init__(self, db_session):
        self.db_session = db_session
        self.customer_use_case = CustomerUseCases(self.db_session)
        
    def create_customer(self, customer):
        
        try:
            customer_use_case = self.customer_use_case.create_customer(customer)

            return JSONResponse(content={'message':'Cliente criado com sucesso'}, status_code=status.HTTP_201_CREATED)
        
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Erro ao criar o cliente")
    
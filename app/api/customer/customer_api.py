from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.drivers.database import get_db_session, token_verifier
from app.schemas.customer.customer_schemas import RegisterCustomerSchema
from app.controllers.customer.customer_controller import CustomerController

router = APIRouter(prefix='/customer', tags=['customer'], dependencies=[Depends(token_verifier)])

@router.post('/create', summary='Cadastrar cliente no sistema')
def create(customer: RegisterCustomerSchema, db_session: Session = Depends(get_db_session)):

    try:
        return CustomerController(db_session=db_session).create_customer(customer=customer)
    except Exception as e:
        raise e 

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.drivers.database import get_db_session, token_verifier
from app.schemas.customer.customer_schemas import CustomerSchemas
from app.controllers.customer.customer_controller import CustomerController

router = APIRouter(prefix='/customer', tags=['customer'], dependencies=[Depends(token_verifier)])

@router.post('/register', summary='Cadastrar cliente no sistema')
def register(customers: CustomerSchemas, db_session: Session = Depends(get_db_session)):
    try:
        return CustomerController(db_session=db_session)
    except Exception as e:
        raise e

from fastapi import status, HTTPException
from fastapi.responses import JSONResponse
from app.use_cases.usuario.user_use_cases import UserUseCases

class CustomerController:
    
    def __init__(self, db_session):
        self.db_session = db_session
        
    
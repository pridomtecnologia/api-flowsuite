from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from decouple import config
from app.gateways.usuario.user_gateway import UserGateway

oauth_scheme = OAuth2PasswordBearer(tokenUrl='/user/login')

try:
    
    DATABASE_URL = config('DATABASE_URL')

    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(bind=engine, autoflush=False)
    
except Exception as e:
    raise e

def get_db_session():
    try:
        session = SessionLocal()
        yield session
    finally:
        session.close()
        
def token_verifier(
    db_session: Session = Depends(get_db_session),
    token = Depends(oauth_scheme)
):
    verifica_token_usuario = UserGateway(db_session=db_session)
    verifica_token_usuario.verify_token(access_token=token)
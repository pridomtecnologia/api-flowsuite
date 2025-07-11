from sqlalchemy import Column, String, Integer, Text
from app.drivers.base import Base

class UsuarioModel(Base):
    
    __tablename__ = 'users'
    
    id_user = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(Text, index=True)
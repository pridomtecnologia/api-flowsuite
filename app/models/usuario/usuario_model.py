from sqlalchemy import Column, String, Integer, Text, DateTime, func
from app.drivers.base import Base

class UsuarioModel(Base):
    
    __tablename__ = 'users'
    
    id_user = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(Text, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
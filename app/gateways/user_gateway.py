from sqlalchemy import Column, String, Integer
from app.drivers.base import Base

class UserGateway(Base):
    
    __tablename__ = 'users'
    
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    username = Column(String, index=True)
    password = Column(String, index=True)
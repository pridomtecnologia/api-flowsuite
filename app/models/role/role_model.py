from sqlalchemy import Column, String, Integer, DateTime, func
from app.drivers.base import Base

class RoleModel(Base):
    
    __tablename__ = 'roles'
    
    id_role = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    role = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
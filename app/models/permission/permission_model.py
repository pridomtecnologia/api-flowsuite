from sqlalchemy import Column, Integer, String, DateTime, func
from app.drivers.base import Base

class PermissionModel(Base):
    __tablename__ = "permissions"

    id_permission = Column(Integer, primary_key=True)
    permission = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

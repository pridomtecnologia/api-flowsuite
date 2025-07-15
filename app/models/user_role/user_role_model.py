from sqlalchemy import Column, Integer, ForeignKey, DateTime, func
from app.drivers.base import Base

class UserRoleModel(Base):
    __tablename__ = "user_roles"

    user_id = Column(Integer, ForeignKey("users.id_user", ondelete="CASCADE"), primary_key=True)
    role_id = Column(Integer, ForeignKey("roles.id_role", ondelete="CASCADE"), primary_key=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

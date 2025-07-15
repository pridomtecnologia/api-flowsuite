from sqlalchemy import Column, Integer, ForeignKey, DateTime, func
from app.drivers.base import Base

class RolePermissionModel(Base):
    __tablename__ = "role_permissions"

    role_id = Column(Integer, ForeignKey("roles.id_role", ondelete="CASCADE"), primary_key=True)
    permission_id = Column(Integer, ForeignKey("permissions.id_permission", ondelete="CASCADE"), primary_key=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

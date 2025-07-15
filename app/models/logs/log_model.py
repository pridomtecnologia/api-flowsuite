from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, JSON
from app.drivers.base import Base

class LogModel(Base):
    __tablename__ = "logs"

    id_log = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id_user"))
    action = Column(String(100), nullable=False)
    data = Column(JSON)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

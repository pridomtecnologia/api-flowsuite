from sqlalchemy import Column, String, Integer, DateTime, func
from app.drivers.base import Base

class TagsModel(Base):

    __tablename__ = 'tags'

    id_tag = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    tag = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
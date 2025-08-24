from sqlalchemy import Column, Integer, DateTime, func
from app.drivers.base import Base

class CadastroTagModel(Base):

    __tablename__ = 'cadastro_tag'

    id_cadastro_tag = Column(Integer, primary_key=True)
    cadastro_id = Column(Integer, nullable=False)
    tag_id = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
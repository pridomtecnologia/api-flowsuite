from sqlalchemy import Column, Integer, String, Text, DateTime, func
from app.drivers.base import Base

class AddressModel(Base):
    __tablename__ = "addresses"

    id_address = Column(Integer, primary_key=True)
    address = Column(String(255), nullable=False)
    bairro = Column(String(255), nullable=False)
    numero = Column(String(10), nullable=False)
    estado = Column(String(255), nullable=False)
    cidade = Column(String(255), nullable=False)
    cep = Column(String(10), nullable=False)
    complemento = Column(Text)
    owner_type = Column(String(150), nullable=False)
    owner_id = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

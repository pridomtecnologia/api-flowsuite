from sqlalchemy import Column, Integer, String, Text, DateTime, func
from app.drivers.base import Base

class CadastroModel(Base):
    __tablename__ = "cadastros"

    id_cadastro = Column(Integer, primary_key=True)
    tag_id = Column(Integer, nullable=False)
    razao_social = Column(String(255), nullable=False)
    nome_fantasia = Column(String(255), nullable=False)
    documento = Column(String(20), nullable=False, unique=True)
    email = Column(String(150), nullable=False, unique=True)
    telefone = Column(String(20), nullable=False)
    responsavel_contato = Column(String(255), nullable=False)
    observacao = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

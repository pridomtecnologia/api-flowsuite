from sqlalchemy import Column, Integer, ForeignKey, DateTime, func
from app.drivers.base import Base

class UserCadastroModel(Base):
    __tablename__ = "user_cadastros"

    id_user_cadastro = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id_user", ondelete="CASCADE"))
    cadastro_id = Column(Integer, ForeignKey("cadastros.id_cadastro", ondelete="CASCADE"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

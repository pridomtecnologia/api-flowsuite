from sqlalchemy import Column, Integer, ForeignKey, DateTime, func
from app.drivers.base import Base

class UserCustomerModel(Base):
    __tablename__ = "user_customers"

    id_user_customer = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id_user", ondelete="CASCADE"))
    customer_id = Column(Integer, ForeignKey("customers.id_customer", ondelete="CASCADE"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

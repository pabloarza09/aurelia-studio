from sqlalchemy import Column, String, Float, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class OrderModel(Base):
    __tablename__ = "orders"

    id = Column(String, primary_key=True, index=True)  # ID de orden externo (ej: ORD-2026-X99)
    platform = Column(String, nullable=False, index=True)  # Etsy, Gumroad, etc.
    product_id = Column(String, nullable=False)
    customer_email = Column(String, nullable=False)
    price_paid = Column(Float, nullable=False)
    currency = Column(String, default="USD")
    created_at = Column(DateTime, default=datetime.utcnow)
    additional_meta = Column(JSON, nullable=True)  # Para guardar payloads completos si es necesario
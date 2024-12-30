from pydantic import BaseModel
from decimal import Decimal
from typing import Optional
from sqlalchemy import Column, Integer, String, Numeric, Text
from sqlalchemy.ext.declarative import declarative_base
from ..session import Base


class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    description = Column(Text)
    category = Column(Text, nullable=False)
    image = Column(Text)
    rating_rate = Column(Numeric(3, 1))
    rating_count = Column(Integer)

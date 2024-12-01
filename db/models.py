from sqlalchemy import Column, Integer, String, Text, DateTime, func, ForeignKey, Float
from sqlalchemy.orm import relationship

from db.engine import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship(Category)

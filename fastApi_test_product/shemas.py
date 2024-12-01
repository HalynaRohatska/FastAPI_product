from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    category_id: int


class ProductCreate(ProductBase):
    pass


class Product(ProductCreate):
    id: int

    class Config:
        from_attributes = True

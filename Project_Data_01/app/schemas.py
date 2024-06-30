from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    price: float
    retailer: str


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True  # Updated for Pydantic v2

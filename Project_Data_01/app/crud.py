from sqlalchemy.orm import Session
from .models import Product
from .schemas import ProductCreate


def get_products(db: Session, name: str = None):
    if name:
        return db.query(Product).filter(Product.name.ilike(f"%{name}%")).all()
    return db.query(Product).all()


def create_product(db: Session, product: ProductCreate):
    db_product = Product(name=product.name, price=product.price, retailer=product.retailer)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

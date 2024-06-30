from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import json
from .database import SessionLocal, init_db
from . import crud, models, schemas

app = FastAPI()

# Initialize the database
init_db()

# Load mock data
with open('data/store_data.json', 'r') as file:
    stores = json.load(file)


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/api/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)


@app.get("/api/products/", response_model=list[schemas.Product])
def read_products(name: str = None, db: Session = Depends(get_db)):
    products = crud.get_products(db, name=name)
    if not products:
        raise HTTPException(status_code=404, detail="Product not found")
    return products


@app.on_event("startup")
def startup_event():
    # Optionally, preload the database with mock data
    db = SessionLocal()
    for store, products in stores.items():
        for product in products:
            db_product = models.Product(name=product["name"], price=product["price"], retailer=store)
            db.add(db_product)
    db.commit()

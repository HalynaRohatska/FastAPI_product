from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import shemas
from db.engine import SessionLocal

app = FastAPI()

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/products/", response_model=list[shemas.Product])
def read_products(skip: int = 0, limit: int = 5, db: Session = Depends(get_db)):
    return crud.get_all_products(skip=skip, limit=limit, db=db)


@app.get("/products/{product_id}/", response_model=shemas.Product)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product_detail(db=db, product_id=product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.post("/products/", response_model=shemas.Product)
def create_product(
        product: shemas.ProductCreate,
        db: Session = Depends(get_db)
):
    return crud.create_product(db=db, product=product)


@app.put("/products/{product_id}/", response_model=shemas.Product)
def update_product(
        product_id: int,
        product_shema: shemas.ProductCreate,
        db: Session = Depends(get_db)
):
    product = crud.update_product(product_id=product_id, product_shema=product_shema, db=db)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.delete("/products/{product_id}/", response_model=dict)
def delete_product(
        product_id: int,
        db: Session = Depends(get_db)
):
    product = crud.delete_product(product_id=product_id, db=db)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"detail": "Product deleted successfully."}


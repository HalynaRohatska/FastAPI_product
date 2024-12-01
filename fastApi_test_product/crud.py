from typing import Optional, List

from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from starlette import status

from db import models
import shemas


def get_all_products(db: Session, skip: int = 0, limit: int = 5) -> List[models.Product]:
    return db.query(models.Product).offset(skip).limit(limit).all()


def get_product_detail(db: Session, product_id: int) -> Optional[models.Product]:
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    return product


def create_product(db: Session, product: shemas.ProductCreate) -> models.Product:
    db_product = models.Product(
        name=product.name,
        description=product.description,
        price=product.price,
        category_id=product.category_id
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


def update_product(
        db: Session,
        product_id: int,
        product_shema: shemas.ProductCreate
) -> models.Product:
    product = db.query(models.Product).filter(models.Product.id == product_id).first()

    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    product.name = product_shema.name
    product.description = product_shema.description
    product.price = product_shema.price
    product.category_id = product_shema.category_id

    db.add(product)
    db.commit()
    db.refresh(product)

    return product


def delete_product(db: Session, product_id: int) -> bool:
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

    db.delete(product)
    db.commit()
    return True

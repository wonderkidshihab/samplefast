from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from Dependencies.db_dependency import get_db
from sqlalchemy.orm import Session
from Schemas.product import ProductBase, ProductCreate, ProductUpdate, ProductDelete
from Models.product import Product

app = APIRouter(
    prefix="/product",
    tags=["Product"],
    responses={404: {"description": "Not found"}},
)


@app.get("/", dependencies=[Depends(get_db)], response_model=List[ProductBase])
def getProducts(db: Session = Depends(get_db)):
    return db.query(Product).all()

@app.get("/{id}", dependencies=[Depends(get_db)])
def getProduct(id: int, db: Session = Depends(get_db)):
    return db.query(Product).filter(Product.id == id).first()

@app.post("/", dependencies=[Depends(get_db)])
def createProduct(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = Product(name=product.name, description=product.description, price=product.price, currency=product.currency)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@app.put("/{id}", dependencies=[Depends(get_db)])
def updateProduct(id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == id).first()
    if db_product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db_product.currency = product.currency
    db.commit()
    db.refresh(db_product)
    return db_product

@app.delete("/{id}", dependencies=[Depends(get_db)])
def deleteProduct(id: int, product: ProductDelete, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == id).first()
    if db_product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return {"message": "Product deleted successfully"}

@app.get("/search", dependencies=[Depends(get_db)])
def searchProduct(query: str, db: Session = Depends(get_db)):
    return db.query(Product).filter(Product.name.like(f"%{query}%")).all()

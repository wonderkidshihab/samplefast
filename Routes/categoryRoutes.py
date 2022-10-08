from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from Dependencies.db_dependency import get_db
from sqlalchemy.orm import Session
from Schemas.category import CategoryBase, CategoryCreate, CategoryUpdate, CategoryDelete
from Models.category import Category

app = APIRouter(
    prefix="/category",
    tags=["Category"],
    responses={404: {"description": "Not found"}},
)


@app.get("/", dependencies=[Depends(get_db)], response_model=List[CategoryBase])
def getCategories(db: Session = Depends(get_db)):
    return db.query(Category).all()

@app.get("/{id}", dependencies=[Depends(get_db)])
def getCategory(id: int, db: Session = Depends(get_db)):
    return db.query(Category).filter(Category.id == id).first()

@app.post("/", dependencies=[Depends(get_db)])
def createCategory(category: CategoryCreate, db: Session = Depends(get_db)):
    new_category = Category(name=category.name, description=category.description)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

@app.put("/{id}", dependencies=[Depends(get_db)])
def updateCategory(id: int, category: CategoryUpdate, db: Session = Depends(get_db)):
    db_category = db.query(Category).filter(Category.id == id).first()
    if db_category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    db_category.name = category.name
    db_category.description = category.description
    db.commit()
    db.refresh(db_category)
    return db_category

@app.delete("/{id}", dependencies=[Depends(get_db)])
def deleteCategory(id: int, category: CategoryDelete, db: Session = Depends(get_db)):
    db_category = db.query(Category).filter(Category.id == id).first()
    if db_category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    db.delete(db_category)
    db.commit()
    return {"message": "Category deleted successfully"}

@app.get("/search", dependencies=[Depends(get_db)])
def searchCategory(query: str, db: Session = Depends(get_db)):
    return db.query(Category).filter(Category.name.like(f"%{query}%")).all()
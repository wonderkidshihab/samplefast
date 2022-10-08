from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from Models.users import User
from Schemas.users import UserBase, UserCreate, UserUpdate, UserDelete
from Dependencies.db_dependency import get_db
from sqlalchemy.orm import Session
app = APIRouter(
    prefix="/user",
    tags=["User"],
    responses={404: {"description": "Not found"}},
    
)


@app.get("/", dependencies=[Depends(get_db)], response_model=List[UserBase])
def getUsers(db: Session = Depends(get_db)):
    return db.query(User).all()

@app.get("/{id}", dependencies=[Depends(get_db)])
def getUser(id: int, db: Session = Depends(get_db)):
    return db.query(User).filter(User.id == id).first()

@app.post("/", dependencies=[Depends(get_db)])
def createUser(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(username=user.username, email=user.email, password=user.password, admin=user.admin)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

from pydantic import BaseModel
from typing import Optional, List, Dict, Any, Union
from datetime import datetime

class UserBase(BaseModel):
    id: int
    username: str
    email: str
    created_on: datetime
    admin: bool

    class Config:
        orm_mode = True
        
class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    admin: bool = False


class UserUpdate(BaseModel):
    username: str
    email: str
    password: str
    admin: bool = False

    class Config:
        orm_mode = True
        
class UserDelete(BaseModel):
    id: int



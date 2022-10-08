
from locale import currency
from pydantic import BaseModel
from typing import Optional, List, Dict, Any, Union
from datetime import datetime


class ProductBase(BaseModel):
    id: int
    name: str
    description: str
    price: float
    created_on: datetime
    updated_on: datetime
    currency: str

    class Config:
        orm_mode = True
        
class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    currency: str
    
class ProductUpdate(BaseModel):
    name: str
    description: str
    price: float
    currency: str

    class Config:
        orm_mode = True
        
class ProductDelete(BaseModel):
    pass
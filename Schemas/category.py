from locale import currency
from pydantic import BaseModel
from typing import Optional, List, Dict, Any, Union
from datetime import datetime

class CategoryBase(BaseModel):
    id: int
    name: str
    description: str
    created_on: datetime
    updated_on: datetime

    class Config:
        orm_mode = True
        
class CategoryCreate(BaseModel):
    name: str
    description: str
    
class CategoryUpdate(BaseModel):
    name: str
    description: str

    class Config:
        orm_mode = True
        
class CategoryDelete(BaseModel):
    pass
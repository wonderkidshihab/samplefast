from email.policy import default
from locale import currency
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from Database.database import Base

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(120), unique=True, nullable=False)
    created_on = Column(DateTime(timezone=True), server_default=func.now())
    updated_on = Column(DateTime(timezone=True), server_default=func.now())
    products = relationship("Product", back_populates="category")

    def __repr__(self):
        return f"Category('{self.name}', '{self.description}', '{self.created_on}')"
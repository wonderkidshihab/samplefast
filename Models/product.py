from email.policy import default
from locale import currency
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from Database.database import Base


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(120), unique=True, nullable=False)
    price = Column(String(120), nullable=False)
    created_on = Column(DateTime(timezone=True), server_default=func.now())
    offerPrice = Column(String(120))
    updated_on = Column(DateTime(timezone=True), server_default=func.now())
    currency = Column(String(120), default='$')
    thumbnail = Column(String(120), nullable=True)
    images = Column(String(120), nullable=True)
    # add a relationship to the Category model here. Every product belongs to a category
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="products")
    
    
    
    

    def __repr__(self):
        return f"Product('{self.name}', '{self.description}', '{self.created_on}')"
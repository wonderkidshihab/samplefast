from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from Database.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    created_on = Column(DateTime(timezone=True), server_default=func.now())
    admin = Column(Boolean, default=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.created_on}')"
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base =  declarative_base()

class ProductModel (Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255),index=True)
    description = Column(String(255),index=True)
    price = Column(String(255))
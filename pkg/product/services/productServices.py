from sqlalchemy.orm import Session
from pkg.product.models.productModel import ProductModel
from pkg.product.schemas.createProduct import ProductCreate

def get_item(db: Session, id: int):
    return db.query(ProductModel).filter(ProductModel.id == id).first()

def get_items(db: Session, skip: int = 0, limit: int = 0):
    return db.query(ProductModel).offset(skip).limit(limit).all()

def store_data(db: Session, product: ProductCreate ):
    db_product = ProductModel(
        name=product.name, 
        description=product.description, 
        price=product.price
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
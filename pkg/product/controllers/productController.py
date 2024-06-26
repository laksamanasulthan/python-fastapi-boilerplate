from config.database import SessionLocal
from fastapi import APIRouter, Depends, HTTPException # type: ignore
from sqlalchemy.orm import Session
from pkg.product.schemas.createProduct import ProductCreate
from pkg.product.services import productServices

router = APIRouter()

def conn_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[ProductCreate])
def index(skip: int = 0, limit: int = 10, db: Session = Depends(conn_db)):
    items = productServices.get_items(db, skip=skip, limit=limit)
    return items


@router.get("/{id}", response_model = ProductCreate)
def get_by_id (id:int, db: Session = Depends(conn_db)):
    db_product = productServices.get_item(
        db=db, 
        id=id
    )
    if db_product is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_product

@router.post("/", response_model = ProductCreate)
def store_data (product: ProductCreate, db: Session = Depends(conn_db)):
    db_product = productServices.store_data(
        db = db,
        product = product
    )
    if db_product is None:
        raise HTTPException(status_code=400, detail="Failed Create Product")
    return db_product
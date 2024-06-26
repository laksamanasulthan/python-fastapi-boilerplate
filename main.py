from pathlib import Path
from typing import Union
from dotenv import load_dotenv
from fastapi import FastAPI # type: ignore
from pkg.product.controllers import productController
from pkg.product.models import productModel
from config.database import engine
from routes.routes import configure_router
from config.database import initalize_database

initalize_database()

app = FastAPI()

configure_router(app)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
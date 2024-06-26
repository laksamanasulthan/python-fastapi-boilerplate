from fastapi import APIRouter
from pkg.product.controllers import productController  


def configure_router(app):
    app.include_router(productController.router, prefix="/product", tags= ['product'])
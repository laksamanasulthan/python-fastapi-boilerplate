from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker
import os
from pkg.product.models.productModel import Base as ProductBase

env_path = Path('.') / '.env'

load_dotenv(dotenv_path=env_path)


# URL_DATABASE = os.getenv("URL_DATABASE")

URL_DATABASE = URL.create(
    os.getenv("DIALECT_AND_DRIVER"),
    username= os.getenv("DB_USERNAME"),
    password= os.getenv("DB_PASSWORD"),
    host= os.getenv("DB_HOST"),
    port= os.getenv("DB_PORT"),
    database= os.getenv("DB_DATABASE"),
)

if URL_DATABASE is None:
    raise ValueError("URL_DATABASE is not set in the environment.")


engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def initalize_database():
    ProductBase.metadata.create_all(bind=engine)
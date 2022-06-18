import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, '.env'))

# Get environment variables from .env file
DATABASE_URL = os.getenv("DATABASE_URL")

print('config DATABASE_URL:', DATABASE_URL)

app.add_middleware(DBSessionMiddleware, db_url=DATABASE_URL)

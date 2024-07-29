from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from redis_om import get_redis_connection, HashModel
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers = ['*']
    )

redis = get_redis_connection(
    host = os.getenv("REDIS_HOST"),
    port = os.getenv("REDIS_PORT"),
    password = os.getenv("REDIS_PASSWORD"),
    decode_responses = True
)

class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis

@app.get("/products")
async def all():
    return Product.all_pks
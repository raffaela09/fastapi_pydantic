from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
app = FastAPI()

books = []

class Book(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float


app = FastAPI()
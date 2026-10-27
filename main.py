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

@app.get("/")
async def root():
    return {"Mensagem": "Sistema de Livraria Online"}

@app.post("/books/", response_model=Book, status_code=status.HTTP_201_CREATED)
async def create_book(book: Book):
    for b in books: # Mudei de "book" para "b"
        # validação de que o livro já existe
        if b.id == book.id: 
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Livro com este ID já existe.")
            
    # caso não exista, adiciona o livro na lista
    books.append(book)
    return book

#retorna todos os livros cadastrados
@app.get("/books/")
async def get_all_books():
    return books

@app.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Livro não encontrado.")
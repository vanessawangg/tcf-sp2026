from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI()

# --- Mock Database ---
# We will use this list to store our data in-memory.
# Each book is a dictionary: {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937}
books_db = []

# --- Pydantic Models ---
# This class defines the structure of the data we expect from the client.
# TODO: Students need to understand why we use this.
class BookCreate(BaseModel):
    title: str
    author: str
    year: int

class Book(BookCreate):
    id: int

# --- Routes ---

@app.get("/")
def read_root():
    return {"message": "Welcome to the Library API. Go to /docs to test the endpoints."}

# TODO: Implement the GET /books endpoint
# Requirements:
# 1. Return all books.
# 2. Support a query parameter 'author' to filter books by a specific author.
#    - Example: /books?author=Orwell
@app.get("/books", response_model=List[Book])
def get_books(author: Optional[str] = Query(None)):
    if author:
        return [book for book in books_db if book["author"] == author]
    return books_db

# TODO: Implement the POST /books endpoint
# Requirements:
# 1. Accept a book in the request body (use the BookCreate model).
# 2. Generate a unique ID for the book (incrementing from the last ID or using UUID).
# 3. Add the book to books_db.
# 4. Return the created book object.
@app.post("/books", response_model=Book)
def create_book(book: BookCreate):
    if books_db:
        new_id = max(b["id"] for b in books_db) + 1
    else:
        new_id = 1

    new_book = {
        "id": new_id,
        "title": book.title,
        "author": book.author,
        "year": book.year
    }

    books_db.append(new_book)
    return new_book

# TODO: Implement the GET /books/{book_id} endpoint
# Requirements:
# 1. Return the book with the matching ID.
# 2. If the book is not found, raise an HTTPException with status code 404.
@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books_db:
        if book["id"] == book_id:
            return book

    raise HTTPException(status_code=404, detail="Book not found")

# TODO: Implement the PUT /books/{book_id} endpoint
# Requirements:
# 1. Update the book with the matching ID using the data from the request body.
# 2. If the book is not found, raise a 404 error.
# 3. Return the updated book.
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_update: BookCreate):
    for book in books_db:
        if book["id"] == book_id:
            book["title"] = book_update.title
            book["author"] = book_update.author
            book["year"] = book_update.year
            return book

    raise HTTPException(status_code=404, detail="Book not found")

# TODO: Implement the DELETE /books/{book_id} endpoint
# Requirements:
# 1. Remove the book with the matching ID from the database.
# 2. If the book is not found, raise a 404 error.
# 3. Return a success message or the deleted book.
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, book in enumerate(books_db):
        if book["id"] == book_id:
            books_db.pop(i)
            return {"message": "Book deleted"}

    raise HTTPException(status_code=404, detail="Book not found")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

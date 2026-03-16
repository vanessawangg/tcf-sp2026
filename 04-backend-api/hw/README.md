# Homework 5: The Personal Library API

**Objective**: Build a robust RESTful API using Python and **FastAPI** to manage a personal book collection.

This assignment introduces you to **FastAPI**, a modern, fast (high-performance) web framework for building APIs with Python 3.8+ based on standard Python type hints.

## 1. Environment Setup

Before writing code, you need to set up your Python environment.

### Step A: Install Python

Check if you have Python installed:

```bash
python3 --version
```

If not, download and install it from [python.org](https://www.python.org/downloads/).

### Step B: Create a Virtual Environment (Recommended)

It is best practice to use a virtual environment to keep your project dependencies isolated.

1.  Navigate to the `hw/` folder in your terminal.
2.  Create the virtual environment (optional, you can choose to install the dependencies globally on your entire computer as well):
    ```bash
    python3 -m venv venv
    ```
3.  Activate the virtual environment:
    - **Mac/Linux**: `source venv/bin/activate`
    - **Windows**: `venv\Scripts\activate`

### Step C: Install Dependencies

You need `fastapi` for the code and `uvicorn` to run the server.

```bash
pip install fastapi uvicorn
```

## 2. Running the Starter Code

1.  Make sure you are in the `hw/` folder and your virtual environment is active.
2.  Run the server:

    ```bash
    python3 main.py
    ```

    - This will start the server on `http://127.0.0.1:8000` with hot-reloading enabled.

3.  Open your browser to `http://localhost:8000`. You should see the welcome message.
4.  **The Magic**: Go to `http://localhost:8000/docs`. FastAPI automatically generates interactive API documentation (Swagger UI). You will use this to test your API.

## 3. The Assignment

Open `main.py`. You will see a skeleton of an API with `TODO` comments. Your goal is to implement the logic for a CRUD (Create, Read, Update, Delete) API for a Library system.

### Data Structure

We are using a simple in-memory list `books_db` to store our data. Each book object looks like this:

```json
{
  "id": 1,
  "title": "1984",
  "author": "George Orwell",
  "year": 1949
}
```

### Tasks

#### Task 1: `GET /books` with Filtering

- Implement the logic to return all books.
- **Tricky Part**: The function accepts an optional `author` query parameter.
- If `?author=Name` is provided in the URL, return only the books by that author.
- If no author is provided, return all books.

#### Task 2: `POST /books`

- Accept a JSON body with `title`, `author`, and `year`.
- **Logic**:
  1.  Generate a new `id`. It should be unique (e.g., find the max ID in the current list and add 1).
  2.  Create the full book dictionary (including the new ID).
  3.  Append it to `books_db`.
  4.  Return the new book.

#### Task 3: `GET /books/{book_id}`

- Find the book with the specific `id` passed in the URL path.
- **Error Handling**: If the book does not exist, you **must** raise an `HTTPException` with status code `404` and a detail message "Book not found".

#### Task 4: `PUT /books/{book_id}`

- Update an existing book.
- Find the book by `id`. Update its `title`, `author`, and `year` with the new data provided.
- **Error Handling**: Raise 404 if the book ID doesn't exist.

#### Task 5: `DELETE /books/{book_id}`

- Remove the book from the list.
- **Error Handling**: Raise 404 if the book ID doesn't exist.

## 4. Concepts found in this HW:

- **Type Hints**: FastAPI relies heavily on Python type hints (e.g., `book_id: int`, `q: Optional[str]`). This validates data automatically. If a user sends "abc" as an ID, FastAPI will automatically return a generic error.
- **Pydantic Models**: We use `BookCreate` (a Pydantic model) to define the "shape" of data we expect. This is similar to defining an interface in TypeScript. You all should be familiar with Interface design from Fundies
- **Status Codes**: You explicitly handle errors (404 Not Found) instead of the server just crashing or returning empty data.

## Submission

Submit your completed `main.py` file.

**Bonus Challenge**: Add a `PATCH` endpoint that allows updating _only_ the title or the author without sending the whole object.

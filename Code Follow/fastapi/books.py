from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()


class Book():
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: Optional[int] = Field(description='ID is not needed', default=None)
    title: str = Field(min_length=3, max_length=100)
    author: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=3, max_length=100)
    rating: int = Field(gt=1, lt=5)

    model_config = {
        'json_schema_extra': {
            'example': {
                "title": "To Kill a Mockingbird",
                "author": "Harper Lee",
                "description": "A novel about racial injustice in the Deep South.",
                "rating": 5
            }
        }
    }


BOOKS = [
    Book(1, "To Kill a Mockingbird", "Harper Lee",
         "A novel about racial injustice in the Deep South.", 5),
    Book(2, "1984", "George Orwell",
         "A dystopian novel about totalitarianism and surveillance.", 5),
    Book(3, "The Great Gatsby", "F. Scott Fitzgerald",
         "A critique of the American Dream set in the 1920s.", 4),
    Book(4, "Moby-Dick", "Herman Melville",
         "The quest for revenge against the white whale.", 4),
    Book(5, "Pride and Prejudice", "Jane Austen",
         "A classic romance novel exploring themes of love and class.", 5),
    Book(6, "The Catcher in the Rye", "J.D. Salinger",
         "A novel about teenage alienation and angst.", 4),
    Book(7, "Brave New World", "Aldous Huxley",
         "A dystopian novel exploring a future society controlled by technology.", 5),
    Book(8, "War and Peace", "Leo Tolstoy",
         "An epic novel about Russian society during the Napoleonic era.", 5),
    Book(9, "The Hobbit", "J.R.R. Tolkien",
         "A fantasy novel about Bilbo Baggins' adventure.", 5),
    Book(10, "Crime and Punishment", "Fyodor Dostoevsky",
         "A psychological novel about guilt and redemption.", 5),
    Book(11, "The Odyssey", "Homer",
         "An epic poem about Odysseus' journey home.", 4),
    Book(12, "Frankenstein", "Mary Shelley",
         "A gothic novel about the dangers of playing god.", 4)
]


@app.get('/books')
async def read_all_books():
    return BOOKS


@app.get("/books/{book_id}")
async def read_book(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book


@app.get("/books/",)
async def read_book_by_rating(book_rating: int):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return


@app.put("/books/update_book")
async def update_book(book: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book


@app.post('/create-books')
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    new_book.id = find_book_id(new_book)
    BOOKS.append(new_book)
    return new_book


def find_book_id(book: Book):
    id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return id

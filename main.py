from fastapi_sqlalchemy import db

from settings import app
from models import Book, Author
from schema import BookSchema, AuthorSchema


@app.get('/')
async def root():
    return {'message': 'Hello JOmba'}


@app.post('/create-book/', response_model=BookSchema)
async def create_book(book: BookSchema):
    book = Book(**book.dict())
    db.session.add(book)
    db.session.commit()
    return book


@app.post('/create-author/', response_model=AuthorSchema)
async def create_author(author: AuthorSchema):
    author = Author(**author.dict())
    db.session.add(author)
    db.session.commit()
    return author


@app.get('/books/')
async def get_books():
    return db.session.query(Book).all()


@app.get('/authors/')
async def get_authors():
    return db.session.query(Author).all()
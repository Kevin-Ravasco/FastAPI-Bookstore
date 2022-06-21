from fastapi import status, HTTPException
from fastapi_sqlalchemy import db

from settings import app
from .models import Book, Author
from .schema import BookSchema, AuthorSchema


@app.get('/')
async def get_books():
    """Returns all the books available"""
    return db.session.query(Book).all()


@app.get('/authors/', )
async def get_authors():
    """Returns all the authors"""
    return db.session.query(Author).all()


@app.post('/create-book/', response_model=BookSchema, status_code=status.HTTP_201_CREATED)
async def create_book(book: BookSchema):
    """Creates a new book"""

    book = Book(**book.dict())
    db.session.add(book)
    db.session.commit()
    return book


@app.post('/create-author/', response_model=AuthorSchema, status_code=status.HTTP_201_CREATED)
async def create_author(author: AuthorSchema):
    """Creates a new author"""

    author = Author(**author.dict())
    db.session.add(author)
    db.session.commit()
    return author


@app.get('/book/{book_id}/', response_model=BookSchema)
async def get_book(book_id: int):
    """Returns a book by id"""
    book = db.session.query(Book).get(book_id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book


@app.get('/author/{author_id}/', response_model=AuthorSchema)
async def get_author(author_id: int):
    """Returns an author by id"""
    author = db.session.query(Author).get(author_id)
    if not author:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Author not found")
    return author


@app.put('/book/{book_id}/', response_model=BookSchema)
async def update_book(book_id: int, book: BookSchema):
    """Updates a book by id"""
    db_book = db.session.query(Book).get(book_id)
    if not db_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    db_book.title = book.title
    db_book.description = book.description
    db_book.rating = book.rating
    db_book.author_id = book.author_id
    db.session.commit()
    return db_book


@app.put('/author/{author_id}/', response_model=AuthorSchema)
async def update_author(author_id: int, author: AuthorSchema):
    """Updates an author by id"""
    db_author = db.session.query(Author).get(author_id)
    if not db_author:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Author not found")
    db_author.name = author.name
    db_author.email = author.email
    db_author.bio = author.bio
    db.session.commit()
    return author


@app.delete('/book/{book_id}/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    """Deletes a book by id"""
    db_book = db.session.query(Book).get(book_id)
    if not db_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    db.session.delete(db_book)
    db.session.commit()
    return


@app.delete('author/{author_id}/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_author(author_id: int):
    """Deletes an author by id"""
    db_author = db.session.query(Author).get(author_id)
    if not db_author:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Author not found")
    db.session.delete(db_author)
    db.session.commit()
    return


@app.get('/author/{author_id}/books/')
async def get_author_books(author_id: int):
    """Returns all the books by an author"""
    author = db.session.query(Author).get(author_id)
    if not author:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Author not found")
    # author_books = db.session.query(Book).filter(Book.author_id == author_id).all()
    return author.books


@app.get('/books/top-rated/')
async def get_top_rated_books():
    """
    Returns books with a rating greater than or equal to 4
    :return Book:
    """
    top_books = db.session.query(Book).filter(Book.rating >= 4).all()
    return top_books

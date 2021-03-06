import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class AuthorSchema(BaseModel):
    name: str
    email: EmailStr
    bio: str
    date_created: Optional[datetime.datetime]
    date_modified: Optional[datetime.datetime]

    class Config:
        orm_mode = True


class BookSchema(BaseModel):
    title: str
    description: str
    rating: int
    author_id: int

    class Config:
        orm_mode = True

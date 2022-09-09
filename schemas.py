from typing import List, Union

import uuid

from fastapi_users import schemas
from pydantic import BaseModel


class UserRead(schemas.BaseUser[uuid.UUID]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass


class User(BaseModel):
    id: int
    name: str
    age: int
    email: str

    class Config:
        orm_mode = True


class Game(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

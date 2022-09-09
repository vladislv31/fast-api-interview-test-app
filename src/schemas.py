from typing import List

from pydantic import BaseModel, EmailStr, validator


class Game(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    email: EmailStr
    age: int

    @validator("age")
    def age_range(cls, value):
        if not (0 <= int(value) <= 100):
            raise ValueError("age should be in range 0-100.")
        return value


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class GameWithUsers(Game):
    users: List[User]


class UserWithGames(User):
    games: List[Game]


class Token(BaseModel):
    access_token: str
    token_type: str

class Login(BaseModel):
    email: str
    password: str

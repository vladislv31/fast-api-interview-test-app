from sqlalchemy.orm import Session

import models, schemas

from auth import hash_password


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = hash_password(user.password)
    db_user = models.User(email=user.email, name=user.name, age=user.age, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_games(db: Session):
    return db.query(models.Game).all()


def get_game_by_id(db: Session, id: int):
    return db.query(models.Game).filter(models.Game.id == id).first()

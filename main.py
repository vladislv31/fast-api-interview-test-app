from typing import List

from fastapi import Depends, FastAPI, HTTPException, status

from sqlalchemy.orm import Session

import crud, models, schemas
from database import engine, get_db

from auth import verify_password, create_access_token, get_current_user


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/login", response_model=schemas.Token)
def login(login: schemas.Login, db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, login.email)
    if user is None or not verify_password(login.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    return schemas.Token(
        access_token=create_access_token({"sub": user.email}),
        token_type="Bearer"
    )


@app.post("/register", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/me", response_model=schemas.UserWithGames)
def user_info(user: models.User = Depends(get_current_user)):
    return user


@app.get("/games", response_model=List[schemas.GameWithUsers])
def games_list(db: Session = Depends(get_db)):
    return crud.get_games(db=db)


@app.post("/conect")
def connect_to_game(id: int, db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    game = crud.get_game_by_id(db=db, id=id)
    if not game:
        raise HTTPException(status_code=400, detail="Game with such id not found")
    user.games.append(game)
    db.add(user)
    db.commit()
    return "Game was connected."



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

from database import SessionLocal
from models import Game


db = SessionLocal()


games = ["tictactoe", "chess", "ctf", "football", "basketball", "dota2", "csgo"]

for game_name in games:
    game = Game(name=game_name)
    db.add(game)

db.commit()
db.close()

## Test FastAPI App

### Important Notes

It's my first application that I developed using FastAPI. I understand that there is many bad practices and other problems in code.

### Task

Part 1:

* Create FastAPI base project
* Create User model (id, name, age(min=0, max=100), email)
* Create Game model (id, name)
* Create Endpoints:
	- Get games (get list of all games and users who connected to this games)
	- Get me (get info about current user and info about all connected games)
	- Connect to game. When user send this request. Need to create one obj like User - Game.

Part 2 (Advanced):

- Use SQLAlchemy for store your models
-Use docker for run your code

### Environment

You should create .env file(look .env.example).

### Commands

- To run: `docker-compose up --build d` (You may run it repeatedly if app not starting because of web not waiting for db)
- To seed db: `docker-compose run web python init_db.py`

Then you can use docs with: http://localhost:8000/docs

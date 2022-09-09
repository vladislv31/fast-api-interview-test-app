## Test FastAPI App

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

### Commands

- To run: `docker-compose up --build d`
- To seed db: `docker-compose run web python init_db.py`

Then you can use docs with: http://localhost:8000/docs

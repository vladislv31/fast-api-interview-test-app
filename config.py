from starlette.config import Config

config = Config(".env")

DATABASE_URL = config("DATABASE_URL", cast=str)
ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = "HS256"
SECRET_KEY = config("SECRET_KEY", cast=str)

import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL", "sqlite:///./test.db"
)  # Example with SQLite, change for production DB
# for postgresql
# DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/db_name")
SECRET_KEY = os.getenv("SECRET_KEY", "a7a492562c8d2a4b153b13ee5912e9eb83047ff8")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = 30

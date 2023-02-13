import os
from dotenv import load_dotenv

#env_path = Path('..') / '.env'
env_path ='.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    MYSQL_DATABASE: str = os.getenv("MYSQL_DATABASE")
    MYSQL_USER: str = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD")
    MYSQL_PORT: str = os.getenv("MYSQL_PORT")

settings = Settings()
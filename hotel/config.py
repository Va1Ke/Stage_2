import os
from dotenv import load_dotenv, find_dotenv

#ENV_PATH = '../.env'
load_dotenv(dotenv_path=find_dotenv('.env'))

class Settings:
    """Accessing the env data through the class"""
    MYSQL_DATABASE: str = os.getenv("MYSQL_DATABASE")
    MYSQL_USER: str = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD")
    MYSQL_PORT: str = os.getenv("MYSQL_PORT")

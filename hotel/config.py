import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(dotenv_path=find_dotenv('../.env'))

class Settings:
    """Accessing the env data through the class"""
    MYSQL_DATABASE: str = os.getenv("MYSQL_DATABASE")
    MYSQL_USER: str = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD")
    MYSQL_PORT: str = os.getenv("MYSQL_PORT")
    #SQLALCHEMY_DATABASE_URL: str = 'mysql+pymysql://' + MYSQL_USER + ':' + MYSQL_PASSWORD + \
    #                          '@db:' + MYSQL_PORT + '/' + MYSQL_DATABASE
    SQLALCHEMY_DATABASE_URL: str = 'mysql+pymysql://' + MYSQL_USER + ':' + MYSQL_PASSWORD + \
                                   '@127.0.0.1:' + MYSQL_PORT + '/' + MYSQL_DATABASE
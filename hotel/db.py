from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from config import Settings
import databases

SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://' + Settings.MYSQL_USER + ':' + Settings.MYSQL_PASSWORD + \
                                       '@db:' + Settings.MYSQL_PORT + '/' + Settings.MYSQL_DATABASE
db = databases.Database(SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()

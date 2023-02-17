from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from hotel.config import Settings
from flask_migrate import Migrate

app = Flask(__name__)

app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + Settings.MYSQL_USER + ':' + Settings.MYSQL_PASSWORD + \
                                        '@db:' + Settings.MYSQL_PORT + '/' + Settings.MYSQL_DATABASE
db = SQLAlchemy(app)
from hotel.models.models import *
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()

import os
from flask_sqlalchemy import SQLAlchemy
from aioflask import Flask
import asyncio
from config import Settings
from views import clients_routes, orders_routes, hotel_routes

SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://' + Settings.MYSQL_USER + ':' + Settings.MYSQL_PASSWORD + \
                                       '@db:' + Settings.MYSQL_PORT + '/' + Settings.MYSQL_DATABASE
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from models.models import *
app.register_blueprint(clients_routes.clients_rout)
app.register_blueprint(orders_routes.orders_rout)
app.register_blueprint(hotel_routes.hotel_rout)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

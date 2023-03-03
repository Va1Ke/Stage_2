import logging
from flask import Flask
from flask.logging import default_handler
from flask_restful import Api
from hotel.config import Settings
from hotel.rest import client_api, hotel_api
def create_app():
    """flask main def"""
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler('log/logs.log')
    file_handler.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(default_handler)

    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = Settings.SQLALCHEMY_DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    api = Api(app)

    from hotel.models.models import db, migrate
    db.init_app(app)
    migrate.init_app(app, db)

    from hotel.views import clients_routes, hotel_routes

    app.register_blueprint(clients_routes.clients_rout)
    app.register_blueprint(hotel_routes.hotel_rout)

    app.register_blueprint(client_api.api_Client_blueprint)
    api.add_resource(client_api.ClientList, '/clients/')
    api.add_resource(client_api.ClientListByPhone, '/clients/<phone_number>/')
    api.add_resource(client_api.ClientDeleteUpdateAdd, '/clients/change/<client_id>/')

    app.register_blueprint(hotel_api.api_Hotel_blueprint)
    api.add_resource(hotel_api.HotelList, '/rooms/')
    api.add_resource(hotel_api.HotelListByFreeAmount, '/rooms/<search_by_free_amount>/')
    api.add_resource(hotel_api.HotelDeleteUpdateAdd, '/rooms/change/<room_id>/')

    return app

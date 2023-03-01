from flask import Flask
from flask_restful import Api
from hotel.config import Settings
from hotel.rest import client_api, hotel_api, orders_api

def create_app():
    """flask main def"""
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = Settings.SQLALCHEMY_DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    api = Api(app)

    from hotel.models.models import db, migrate
    db.init_app(app)
    migrate.init_app(app, db)

    from hotel.views import clients_routes, hotel_routes, orders_routes

    app.register_blueprint(clients_routes.clients_rout)
    app.register_blueprint(hotel_routes.hotel_rout)
    app.register_blueprint(orders_routes.orders_rout)

    app.register_blueprint(client_api.api_Client_blueprint)
    api.add_resource(client_api.ClientList, '/clients/')
    api.add_resource(client_api.ClientListByPhone, '/clients/<phone_number>/')
    api.add_resource(client_api.ClientDeleteUpdateAdd, '/clients/change/<client_id>/')

    app.register_blueprint(hotel_api.api_Hotel_blueprint)
    api.add_resource(hotel_api.HotelList, '/rooms/')
    api.add_resource(hotel_api.HotelListByBusy, '/rooms/<busy>/')
    api.add_resource(hotel_api.HotelDeleteUpdateAdd, '/rooms/change/<room_id>/')

    app.register_blueprint(orders_api.api_Orders_blueprint)
    api.add_resource(orders_api.OrderList, '/orders/')
    api.add_resource(orders_api.OrderListByClient, '/orders/<client_id>/')
    api.add_resource(orders_api.OrderDeleteUpdateAdd, '/orders/change/<order_id>/')

    return app

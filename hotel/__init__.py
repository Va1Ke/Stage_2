from flask import Flask
from hotel.config import Settings


def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = Settings.SQLALCHEMY_DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from hotel.models.models import db, migrate
    db.init_app(app)
    migrate.init_app(app, db)

    from hotel.views import clients_routes, orders_routes, hotel_routes

    app.register_blueprint(clients_routes.clients_rout)
    app.register_blueprint(orders_routes.orders_rout)
    app.register_blueprint(hotel_routes.hotel_rout)

    return app
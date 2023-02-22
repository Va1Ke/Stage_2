from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

class Clients(db.Model):
    __tablename__ = "clients"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    phone_number = db.Column(db.String(128))


class Hotel(db.Model):
    __tablename__ = "hotel"
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.Integer)
    number_of_beds = db.Column(db.Integer)
    price_for_a_night = db.Column(db.Integer)
    busy = db.Column(db.Boolean)


class Orders(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey("clients.id"))
    room_id = db.Column(db.Integer, db.ForeignKey("hotel.id"))
    name = db.Column(db.String(128))
    phone_number = db.Column(db.String(128))
    rented = db.Column(db.String(10))
    on_days = db.Column(db.Integer)


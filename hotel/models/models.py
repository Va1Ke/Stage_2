import json
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

class Clients(db.Model):
    """class for db interaction"""
    __tablename__ = "clients"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    phone_number = db.Column(db.String(128))

    def to_json(self):
        """get client info as json"""
        return json.dumps({
            "id": self.id,
            "name": self.name,
            "phone_number": self.phone_number
        })

class Hotel(db.Model):
    """class for db interaction"""
    __tablename__ = "hotel"
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.Integer)
    number_of_beds = db.Column(db.Integer)
    price_for_a_night = db.Column(db.Integer)
    busy = db.Column(db.Boolean)

    def to_json(self):
        """get room info as json"""
        return json.dumps({
            "room_id": self.id,
            "area": self.area,
            "number_of_beds": self.number_of_beds,
            "price_for_a_night": self.price_for_a_night,
            "busy": self.busy
        })

class Orders(db.Model):
    """class for db interaction"""
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey("clients.id"))
    room_id = db.Column(db.Integer, db.ForeignKey("hotel.id"))
    name = db.Column(db.String(128))
    phone_number = db.Column(db.String(128))
    rented = db.Column(db.String(20))
    renting_ends = db.Column(db.String(20))

    def to_json(self):
        """get order info as json"""
        return json.dumps({
            "order_id": self.id,
            "client_id": self.client_id,
            "room_id": self.room_id,
            "client_name": self.name,
            "client_phone_number": self.phone_number,
            "rented": self.rented,
            "renting_ends": self.renting_ends
        })

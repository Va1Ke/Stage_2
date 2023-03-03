import json
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

class Hotel(db.Model):
    """class for db interaction"""
    __tablename__ = "hotel"
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.Integer, nullable=False)
    price_for_a_night = db.Column(db.Integer, nullable=False)
    max_amount_clients = db.Column(db.Integer, nullable=False)
    free_amount = db.Column(db.Integer, nullable=False)
    number_of_occupied = db.Column(db.Integer, nullable=False)

    def to_json(self):
        """get room info as json"""
        return json.dumps({
            "room_id": self.id,
            "area": self.area,
            "price_for_a_night": self.price_for_a_night,
            "max_amount_clients": self.max_amount_clients,
            "free_amount": self.free_amount,
            "number_of_occupied": self.number_of_occupied
        })

class Clients(db.Model):
    """class for db interaction"""
    __tablename__ = "clients"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    phone_number = db.Column(db.String(128), unique=True, nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey("hotel.id"), nullable=True)

    def to_json(self):
        """get client info as json"""
        return json.dumps({
            "id": self.id,
            "name": self.name,
            "phone_number": self.phone_number,
            "room_id": self.room_id
        })

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from hotel.db import Base

class Clients(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    phone_number = Column(String(128))


clients = Clients.__table__

class Hotel(Base):
    __tablename__ = "hotel"
    id = Column(Integer, primary_key=True)
    area = Column(Integer)
    number_of_beds = Column(Integer)
    price_for_a_night = Column(Integer)
    busy = Column(Boolean)

hotel = Hotel.__table__

class Orders(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    room_id = Column(Integer, ForeignKey("hotel.id"))
    name = Column(String(128))
    phone_number = Column(String(128))
    rented = Column(DateTime)
    on_days = Column(Integer)

orders = Orders.__table__

from hotel.service.schemas import hotel_schemas
from hotel.models.models import Hotel, Clients
from hotel.models.models import db


def get_all_rooms() -> list[Hotel]:
    """get all rooms list"""
    rooms = Hotel.query.all()
    return rooms

def search_room_by_free_amount(search_by_free_amount: int) -> dict:
    """find a free room"""
    rooms = Hotel.query.filter(Hotel.free_amount >= search_by_free_amount).all()
    return rooms

def add_client_to_room(room_id: int) -> dict:
    """add client to room"""
    room = Hotel.query.filter_by(id=room_id).first()
    if room.max_amount_clients > room.number_of_occupied:
        room.free_amount = room.free_amount - 1
        room.number_of_occupied = room.number_of_occupied + 1
        db.session.commit()
        return {"description": "Success"}
    return {"description": "no free amount in this room"}

def subtract_client_from_room(room_id: int) -> dict:
    """update a room amount"""
    room = Hotel.query.filter_by(id=room_id).first()
    room.free_amount = room.free_amount + 1
    room.number_of_occupied = room.number_of_occupied - 1
    db.session.commit()
    return {"description": "Success"}


def update_rooms_amount() -> dict:
    """update all rooms amount"""
    rooms = Hotel.query.all()
    for room in rooms:
        clients = Clients.query.filter_by(room_id=room.id).all()
        if clients:
            room.number_of_occupied = len(clients)
            room.free_amount = room.max_amount_clients - room.number_of_occupied
            db.session.commit()
    return {"description": "Success"}



def add_room(room: hotel_schemas.AddRoom) -> dict:
    """add room"""
    db_room = Hotel(area=room.area,
                    price_for_a_night=room.price_for_a_night, max_amount_clients=room.max_amount_clients,
                    free_amount=room.max_amount_clients, number_of_occupied=0)
    db.session.add(db_room)
    db.session.commit()
    return {"description": "Success"}


def edit_room(room: hotel_schemas.EditRoomInfo) -> dict:
    """put room info"""
    updated_room = Hotel.query.filter_by(id=room.id).first()
    if updated_room:
        if updated_room.number_of_occupied <= room.max_amount_clients:
            updated_room.area = room.area
            updated_room.price_for_a_night = room.price_for_a_night
            updated_room.max_amount_clients = room.max_amount_clients
            updated_room.free_amount = room.max_amount_clients - updated_room.number_of_occupied
            db.session.commit()
            new_room_info = Hotel.query.filter_by(id=room.id).first()
            return new_room_info
        return {"description": "number_of_occupied must be <= than entered max_amount_clients"}
    return {"description": "no such room"}


def delete_room(room_id: int) -> dict:
    """delete room"""
    room = Hotel.query.filter_by(id=room_id).first()
    if room:
        check = Clients.query.filter_by(room_id=room_id).first()
        if check:
            return {"error": "room is busy"}
        db.session.delete(room)
        db.session.commit()
        return {"description": "Success"}
    return {"description": "no such room"}

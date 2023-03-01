from hotel.service.schemas import hotel_schemas
from hotel.models.models import Hotel, Orders
from hotel.models.models import db


def get_all_rooms() -> list[Hotel]:
    """get all rooms list"""
    rooms = Hotel.query.all()
    if rooms:
        return rooms
    return []


def find_room(busy: int) -> list[Hotel]:
    """find free rooms"""
    room = Hotel.query.filter_by(busy=busy).all()
    if room:
        return room
    return []


def add_room(room: hotel_schemas.AddRoom) -> dict:
    """add room"""
    db_room = Hotel(area=room.area, number_of_beds=room.number_of_beds,
                    price_for_a_night=room.price_for_a_night, busy=False)
    db.session.add(db_room)
    db.session.commit()
    return {"Status_code": "200", "description": "Success"}


def edit_room(room: hotel_schemas.EditRoomInfo) -> dict:
    """put room info"""
    updated_room = Hotel.query.filter_by(id=room.id).first()
    if updated_room:
        updated_room.area = room.area
        updated_room.number_of_beds = room.number_of_beds
        updated_room.price_for_a_night = room.price_for_a_night
        updated_room.busy = room.busy
        db.session.commit()
        return updated_room
    return {"Status_code": "400", "description": "no such room"}


def delete_room(room_id: int) -> dict:
    """detel room"""
    check = Orders.query.filter_by(room_id=room_id).first()
    if check:
        return {"Status_code": "400", "description": "order exist with that room"}
    room = Hotel.query.filter_by(id=room_id).first()
    if room:
        db.session.delete(room)
        db.session.commit()
        return {"Status_code": "200", "description": "Success"}
    return {"Status_code": "400", "description": "no such room"}

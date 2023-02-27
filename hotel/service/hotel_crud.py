from http.client import HTTPException
from hotel.service.schemas import hotel_schemas
from hotel.models.models import Hotel, Orders
from hotel.models.models import db


def get_all_rooms() -> list[Hotel]:
    rooms = Hotel.query.all()
    if rooms:
        return rooms
    else:
        raise {"Status_code": "400", "description": "no rooms"}


def find_room(busy: int) -> list[Hotel]:
    room = Hotel.query.filter_by(busy=busy).all()
    if room:
        return room
    else:
        raise {"Status_code": "400", "description": "no free rooms"}


def add_room(room: hotel_schemas.AddRoom) -> dict:
    db_room = Hotel(area=room.area, number_of_beds=room.number_of_beds,
                    price_for_a_night=room.price_for_a_night, busy=False)
    db.session.add(db_room)
    db.session.commit()
    return {"Status_code": "200", "description": "Success"}


def edit_room(room: hotel_schemas.EditRoomInfo) -> dict:
    updated_room = Hotel.query.filter_by(id=room.id).first()
    if updated_room:
        updated_room.area = room.area
        updated_room.number_of_beds = room.number_of_beds
        updated_room.price_for_a_night = room.price_for_a_night
        updated_room.busy = room.busy
        db.session.commit()
        return updated_room
    else:
        raise {"Status_code": "400", "description": "no such room"}


def delete_room(room_id: int) -> dict:
    check = Orders.query.filter_by(room_id=room_id).first()
    if check:
        raise {"Status_code": "400", "description": "order exist with that room"}
    room = Hotel.query.filter_by(id=room_id).first()
    if room:
        db.session.delete(room)
        db.session.commit()
        return {"Status_code": "200", "description": "Success"}
    else:
        raise {"Status_code": "400", "description": "no such room"}

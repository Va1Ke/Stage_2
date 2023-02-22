from http.client import HTTPException

from hotel.service.schemas import hotel_schemas
from hotel.models.models import Hotel

class Hotel_crud:

    def __init__(self, db):
        self.db = db

    def add_room(self, room: hotel_schemas.AddRoom) -> str:
        db_room = Hotel(area=room.area, number_of_beds=room.number_of_beds,
                                        price_for_a_night=room.price_for_a_night, busy=False)
        self.db.session.add(db_room)
        self.db.session.commit()
        return "Success"

    def edit_room(self, room: hotel_schemas.EditRoomInfo) -> str:
        updated_room = Hotel.query.filter_by(id=room.id).first()
        updated_room.area = room.area
        updated_room.number_of_beds = room.number_of_beds
        updated_room.price_for_a_night = room.price_for_a_night
        updated_room.busy = room.busy
        self.db.session.commit()
        return "Success"

    def delete_room(self, id: int) -> str:
        room = Hotel.query.filter_by(id=id).first()
        self.db.session.delete(room)
        self.db.session.commit()
        return "Success"


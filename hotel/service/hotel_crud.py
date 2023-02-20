# from hotel.service.schemas import hotel_schemas
# from hotel.models.models import hotel
#
# class Hotel_crud:
#     def __init__(self, db):
#         self.db = db
#
#     async def add_room(self, room: hotel_schemas.AddRoom) -> hotel_schemas.RoomInfoReturn:
#         db_room = hotel.insert().values(area=room.area, number_of_beds=room.number_of_beds,
#                                         price_for_a_night=room.price_for_a_night)
#         record_id = await self.db.execute(db_room)
#         return hotel_schemas.RoomInfoReturn(**room.dict(), id=record_id,)
#

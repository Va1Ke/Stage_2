from pydantic import BaseModel

class RoomInfoReturn(BaseModel):
    id: int
    area: int
    number_of_beds: int
    price_for_a_night: int
    busy: bool

class AddRoom(BaseModel):
    area: int
    number_of_beds: int
    price_for_a_night: int

class EditRoomInfo(BaseModel):
    id: int
    area: int
    number_of_beds: int
    price_for_a_night: int
    busy: bool



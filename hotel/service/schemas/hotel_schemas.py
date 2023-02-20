from pydantic import BaseModel

class RoomInfoReturn(BaseModel):
    id: int
    area: str
    number_of_beds: str
    price_for_a_night: int
    busy: bool

class AddRoom(BaseModel):
    area: str
    number_of_beds: str
    price_for_a_night: int

class EditRoomInfo(BaseModel):
    id: int
    area: str
    number_of_beds: str
    price_for_a_night: int
    busy: bool

class DeleteRoom(BaseModel):
    id: int



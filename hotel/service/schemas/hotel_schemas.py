from pydantic import BaseModel

class RoomInfoReturn(BaseModel):
    id: int
    area: int
    price_for_a_night: int
    max_amount_clients: int
    free_amount: int
    number_of_occupied: int

class AddRoom(BaseModel):
    area: int
    price_for_a_night: int
    max_amount_clients: int

class EditRoomInfo(BaseModel):
    id: int
    area: int
    price_for_a_night: int
    max_amount_clients: int


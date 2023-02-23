from pydantic import BaseModel
import datetime

class OrderInfoReturn(BaseModel):
    id: int
    client_id: int
    room_id: int
    name: str
    phone_number: str
    rented: str
    renting_ends: str

class CreateOrder(BaseModel):
    client_id: int
    room_id: int
    rented: str
    renting_ends: str

class EditOrder(BaseModel):
    id: int
    client_id: int
    room_id: int
    rented: str
    renting_ends: str



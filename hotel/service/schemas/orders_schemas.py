from pydantic import BaseModel
import datetime

class OrderInfoReturn(BaseModel):
    id: int
    client_id: int
    room_id: int
    name: str
    phone_number: str
    rented: str
    on_days: int

class CreateOrder(BaseModel):
    client_id: int
    room_id: int
    rented: str
    on_days: int

class EditOrder(BaseModel):
    id: int
    client_id: int
    room_id: int
    rented: str
    on_days: int



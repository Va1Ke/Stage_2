from pydantic import BaseModel
from typing import Union

class ClientInfoReturn(BaseModel):
    id: int
    name: str
    phone_number: str
    room_id: int

class AddClient(BaseModel):
    name: str
    phone_number: str

class EditClientInfo(BaseModel):
    id: int
    name: str
    phone_number: str
    room_id: Union[int, None]


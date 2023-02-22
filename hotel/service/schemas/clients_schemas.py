from pydantic import BaseModel

class ClientInfoReturn(BaseModel):
    id: int
    name: str
    phone_number: str

class AddClient(BaseModel):
    name: str
    phone_number: str


class EditClientInfo(BaseModel):
    id: int
    name: str
    phone_number: str


from typing import Union
from hotel.service.schemas import clients_schemas
from hotel.models.models import db, Clients
from hotel.service.hotel_crud import add_client_to_room, subtract_client_from_room


def get_all_clients() -> list[Clients]:
    """get all clients list"""
    clients = Clients.query.all()
    return clients


def find_client(phone_number: str) -> Clients:
    """find client by phone_number"""
    client = Clients.query.filter_by(phone_number=phone_number).first()
    if client:
        return client
    return {"Status_code": "400", "description": "no such client"}


def add_client(client: clients_schemas.AddClient) -> Clients:
    """add client"""
    new_client = Clients(name=client.name, phone_number=client.phone_number)
    db.session.add(new_client)
    db.session.commit()
    client = Clients.query.filter_by(phone_number=client.phone_number).first()
    return client


def edit_client(client: clients_schemas.EditClientInfo) -> Union[Clients, dict]:
    """put client info"""
    updated_client = Clients.query.filter_by(id=client.id).first()
    if updated_client:
        updated_client.name = client.name
        updated_client.phone_number = client.phone_number
        if updated_client.room_id is not None and client.room_id is None:
            response = subtract_client_from_room(room_id=updated_client.room_id)
            if isinstance(response, dict) and response.get("description") == "Success":
                updated_client.room_id = None
                db.session.commit()
                client = Clients.query.filter_by(id=client.id).first()
                return client
        elif client.room_id > 0:
            response = add_client_to_room(room_id=client.room_id)
            if isinstance(response, dict) and response.get("description") == "Success":
                updated_client.room_id = client.room_id
                db.session.commit()
                client = Clients.query.filter_by(id=client.id).first()
                return client
        return response
    return {"Status_code": 400, "description": "no such client"}


def delete_client(client_id: int) -> dict:
    """delete client"""
    client = Clients.query.filter_by(id=client_id).first()
    if client:
        if client.room_id:
            subtract_client_from_room(room_id=client.room_id)
        db.session.delete(client)
        db.session.commit()
        return {"description": "Success"}
    return {"description": "no such client"}

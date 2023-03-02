from hotel.service.schemas import clients_schemas
from hotel.models.models import Clients, Orders
from hotel.service.orders_crud import update_client_info
from hotel.models.models import db


def get_all_clients() -> list[Clients]:
    """get all clients list"""
    clients = Clients.query.all()
    return clients


def find_client(phone_number: str):
    """find client by phone_number"""
    client = Clients.query.filter_by(phone_number=phone_number).first()
    if client:
        return client
    return {"Status_code": "400", "description": "no such client"}


def add_client(client: clients_schemas.AddClient):
    """add client"""
    new_client = Clients(name=client.name, phone_number=client.phone_number)
    db.session.add(new_client)
    db.session.commit()
    client = Clients.query.filter_by(phone_number=client.phone_number).first()
    return client


def edit_client(client: clients_schemas.EditClientInfo):
    """put client info"""
    updated_client = Clients.query.filter_by(id=client.id).first()
    if updated_client:
        updated_client.name = client.name
        updated_client.phone_number = client.phone_number
        db.session.commit()
        order = Orders.query.filter_by(client_id=client.id).first()
        if order:
            update_client_info(client_id=client.id, name=client.name,
                                phone_number=client.phone_number)
        client = Clients.query.filter_by(id=client.id).first()
        return client
    return {"Status_code": 400, "description": "no such client"}


def delete_client(client_id: int) -> dict:
    """delete client"""
    check = Orders.query.filter_by(client_id=client_id).first()
    if check:
        return {"Status_code": "400", "description": "order exist with that user"}

    client = Clients.query.filter_by(id=client_id).first()
    if client:
        db.session.delete(client)
        db.session.commit()
        return {"Status_code": "200", "description": "Success"}
    return {"Status_code": "400", "description": "no such client"}

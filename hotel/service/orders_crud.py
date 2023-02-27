from http.client import HTTPException
from hotel.service.schemas import orders_schemas
from hotel.models.models import Orders, Clients
from hotel.models.models import db


def get_all_orders() -> list[Orders]:
    orders = Orders.query.all()
    return orders


def find_orders(client_id: int) -> list[Orders]:
    updated_client = Orders.query.filter_by(client_id=client_id).all()
    return updated_client


def create_order(order: orders_schemas.CreateOrder) -> dict:
    client = Clients.query.filter_by(id=order.client_id).first()
    if client:
        new_order = Orders(client_id=order.client_id, room_id=order.room_id,
                           name=client.name, phone_number=client.phone_number,
                           rented=order.rented, renting_ends=order.renting_ends)
        db.session.add(new_order)
        db.session.commit()
        return {"Status_code": "200", "description": "Success"}
    else:
        raise {"Status_code": "400", "description": "no such client"}


def edit_order(order: orders_schemas.EditOrder) -> dict:
    updated_order = Orders.query.filter_by(id=order.id).first()
    if updated_order:
        updated_order.client_id = order.client_id
        updated_order.room_id = order.room_id
        updated_order.rented = order.rented
        updated_order.renting_ends = order.renting_ends
        db.session.commit()
        return updated_order
    else:
        raise {"Status_code": "400", "description": "no such order"}


def delete_order(order_id: int) -> str:
    order = Orders.query.filter_by(id=order_id).first()
    if order:
        db.session.delete(order)
        db.session.commit()
        return {"Status_code": "200", "description": "Success"}
    else:
        raise {"Status_code": "400", "description": "no such order"}


def update_client_info(client_id: int, name: str, phone_number: str) -> str:
    updated_client_info = Orders.query.filter_by(client_id=client_id).first()
    if updated_client_info:
        updated_client_info.name = name
        updated_client_info.phone_number = phone_number
        db.session.commit()
        return "Success"
    else:
        raise "No order with that client"
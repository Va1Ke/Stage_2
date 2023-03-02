from hotel.service.schemas import orders_schemas
from hotel.models.models import Orders, Clients
from hotel.models.models import db


def get_all_orders() -> list[Orders]:
    """get all orders list"""
    orders = Orders.query.all()
    return orders


def find_orders(client_id: int) -> list[Orders]:
    """find order by client"""
    updated_client = Orders.query.filter_by(client_id=client_id).all()
    return updated_client


def create_order(order: orders_schemas.CreateOrder) -> dict:
    """create order"""
    client = Clients.query.filter_by(id=order.client_id).first()
    if client:
        new_order = Orders(client_id=order.client_id, room_id=order.room_id,
                           name=client.name, phone_number=client.phone_number,
                           rented=order.rented, renting_ends=order.renting_ends)
        db.session.add(new_order)
        db.session.commit()
        return {"Status_code": "200", "description": "Success"}
    return {"Status_code": "400", "description": "no such client"}


def edit_order(order: orders_schemas.EditOrder) -> dict:
    """edit order info"""
    updated_order = Orders.query.filter_by(id=order.id).first()
    if updated_order:
        updated_order.client_id = order.client_id
        updated_order.room_id = order.room_id
        updated_order.rented = order.rented
        updated_order.renting_ends = order.renting_ends
        db.session.commit()
        updated_order_ = Orders.query.filter_by(id=order.id).first()
        return updated_order_
    return {"Status_code": "400", "description": "no such order"}


def delete_order(order_id: int) -> str:
    """delete order"""
    order = Orders.query.filter_by(id=order_id).first()
    if order:
        db.session.delete(order)
        db.session.commit()
        return {"Status_code": "200", "description": "Success"}
    return {"Status_code": "400", "description": "no such order"}


def update_client_info(client_id: int, name: str, phone_number: str) -> str:
    """function to update client info in orders table"""
    updated_client_info = Orders.query.filter_by(client_id=client_id).first()
    if updated_client_info:
        updated_client_info.name = name
        updated_client_info.phone_number = phone_number
        db.session.commit()
        return "Success"
    return "No order with that client"

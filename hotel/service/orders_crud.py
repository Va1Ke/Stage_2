from http.client import HTTPException

from hotel.service.schemas import orders_schemas
from hotel.models.models import Orders, Clients
class Orders_crud:

    def __init__(self, db):
        self.db = db

    def create_order(self, order: orders_schemas.CreateOrder) -> str:
        client = Clients.query.filter_by(id=order.client_id).first()
        new_order = Orders(client_id=order.client_id, room_id=order.room_id, name=client.name,
                           phone_number=client.phone_number, rented=order.rented, on_days=order.on_days)
        self.db.session.add(new_order)
        self.db.session.commit()
        return "Success"

    def edit_order(self, order: orders_schemas.EditOrder) -> str:
        updated_order = Orders.query.filter_by(id=order.id).first()
        updated_order.client_id = order.client_id
        updated_order.room_id = order.room_id
        updated_order.rented = order.rented
        updated_order.on_days = order.on_days
        self.db.session.commit()
        return "Success"

    def delete_order(self, id: int) -> str:
        order = Orders.query.filter_by(id=id).first()
        self.db.session.delete(order)
        self.db.session.commit()
        return "Success"

    def update_client_info(self, client_id: int, name: str, phone_number: str):
        updated_client_info = Orders.query.filter_by(client_id=client_id).first()
        updated_client_info.name = name
        updated_client_info.phone_number = phone_number
        self.db.session.commit()
        return "Success"

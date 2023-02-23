from http.client import HTTPException

from hotel.service.schemas import clients_schemas
from hotel.models.models import Clients, Orders
from hotel.service.orders_crud import Orders_crud

class Clients_crud:

    def __init__(self, db):
        self.db = db

    def get_all_clients(self) -> list[clients_schemas.ClientInfoReturn]:
        clients = Clients.query.all()
        return clients

    def find_client(self, phone_number: str) -> list[clients_schemas.ClientInfoReturn]:
        updated_client = Clients.query.filter_by(phone_number=phone_number).all()
        return updated_client

    def add_client(self, client: clients_schemas.AddClient) -> str:
        new_client = Clients(name=client.name, phone_number=client.phone_number)
        self.db.session.add(new_client)
        self.db.session.commit()
        return "Success"

    def edit_client(self, client: clients_schemas.EditClientInfo) -> str:
        updated_client = Clients.query.filter_by(id=client.id).first()
        updated_client.name = client.name
        updated_client.phone_number = client.phone_number
        self.db.session.commit()
        Orders_crud(db=self.db).update_client_info(client_id=client.id, name= client.name,
                                                   phone_number=client.phone_number)
        return "Success"

    def delete_client(self, id: int) -> str:
        check = Orders.query.filter_by(client_id=id).first()
        if check:
            return "redirect"

        client = Clients.query.filter_by(id=id).first()
        self.db.session.delete(client)
        self.db.session.commit()
        return "Success"


from flask import Blueprint, json
from flask_restful import Resource, request
from hotel.service.clients_crud import get_all_clients, find_client, add_client, edit_client, delete_client
from hotel.service.schemas import clients_schemas

api_Client_blueprint = Blueprint('clients_api', __name__)

class ClientList(Resource):
    """ApiClass for get all clients list and add client"""
    def get(self) -> list:
        """get all clients list"""
        response = get_all_clients()
        if response:
            return [json.loads(client.to_json()) for client in response]
        return {"description": "no clients"}

    def post(self) -> dict:
        """add client"""
        new_client = request.get_json(force=True)
        client = clients_schemas.AddClient(name=new_client.get('name'),
                                            phone_number=new_client.get('phone_number'))
        response = add_client(client=client)
        return json.loads(response.to_json())

class ClientListByPhone(Resource):
    """ApiClass for find client by phone number"""
    def post(self, phone_number: str) -> dict:
        """find client by phone number"""
        response = find_client(phone_number)
        return json.loads(response.to_json())

class ClientDeleteUpdateAdd(Resource):
    """ApiClass for put and delete client"""
    def delete(self, client_id: int) -> dict:
        """delete client"""
        response = delete_client(client_id=client_id)
        if response.get('description') == "Success":
            return {"description": "Success"}
        return {"description": "No such user"}

    def put(self, client_id: int) -> dict:
        """put client"""
        new_info_client = request.get_json(force=True)
        k = new_info_client.get('room_id')
        if new_info_client.get('room_id') == "":
            k = None
        client = clients_schemas.EditClientInfo(id=client_id, name=new_info_client.get('name'),
                                                phone_number=new_info_client.get('phone_number'),
                                                room_id=k)
        response = edit_client(client=client)
        return json.loads(response.to_json())

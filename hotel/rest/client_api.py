from flask import Blueprint
from flask_restful import reqparse, abort, Api, Resource, request
from hotel.service.clients_crud import get_all_clients, find_client, add_client, edit_client, delete_client
from hotel.service.schemas import clients_schemas
import json

api_Client_blueprint = Blueprint('clients_api', __name__)

class ClientList(Resource):
    def get(self) -> list:
        response = get_all_clients()
        return [json.loads(client.to_json()) for client in response]

    def post(self) -> dict:
        new_client = request.get_json(force=True)
        client = clients_schemas.AddClient(name=new_client.get('name'),
                                            phone_number=new_client.get('phone_number'))
        response = add_client(client=client)
        return json.loads(response.to_json())

class ClientListByPhone(Resource):
    def post(self, phone_number: str) -> dict:
        response = find_client(phone_number)
        if type(response) == json:
            return response
        return json.loads(response.to_json())

class ClientDeleteUpdateAdd(Resource):

    def delete(self, client_id: int) -> dict:
        response = delete_client(id=client_id)
        if response == "Success":
            return {"Status_code": "200", "description": "Success"}
        else:
            return {"Status_code": "400", "description": "No such user"}

    def put(self, client_id: int) -> dict:
        new_info_client = request.get_json(force=True)
        client = clients_schemas.EditClientInfo(id=client_id, name=new_info_client.get('name'),
                                                phone_number=new_info_client.get('phone_number'))
        response = edit_client(client=client)
        return json.loads(response.to_json())





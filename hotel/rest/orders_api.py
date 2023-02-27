from flask import Blueprint
from flask_restful import reqparse, abort, Resource, request
from hotel.service.orders_crud import get_all_orders, find_orders, create_order, delete_order, edit_order
from hotel.service.schemas import orders_schemas
import json

api_Orders_blueprint = Blueprint('orders_api', __name__)

class OrderList(Resource):
    def get(self) -> dict:
        response = get_all_orders()
        return [json.loads(order.to_json()) for order in response]

    def post(self) -> dict:
        new_order = request.get_json(force=True)
        order = orders_schemas.CreateOrder(client_id=new_order.get('client_id'), room_id=new_order.get('room_id'),
                                        rented=new_order.get('rented'), renting_ends=new_order.get('renting_ends'))
        response = create_order(order)
        return response

class OrderListByBusy(Resource):
    def post(self, client_id: int) -> list:
        response = find_orders(client_id)
        if type(response) == json:
            return response
        return [json.loads(order.to_json()) for order in response]

class OrderDeleteUpdateAdd(Resource):

    def delete(self, order_id: int) -> dict:
        response = delete_order(order_id=order_id)
        return response

    def put(self, order_id: int) -> dict:
        new_order_info = request.get_json(force=True)
        order = orders_schemas.EditOrder(id=order_id, client_id=new_order_info.get('client_id'),
                                          room_id=new_order_info.get('room_id'),
                                          rented=new_order_info.get('rented'),
                                          renting_ends=new_order_info.get('renting_ends'))
        response = edit_order(order=order)
        return json.loads(response.to_json())



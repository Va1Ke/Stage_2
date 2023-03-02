from flask import Blueprint, json
from flask_restful import Resource, request
from hotel.service.orders_crud import get_all_orders, find_orders, create_order, delete_order, edit_order
from hotel.service.schemas import orders_schemas

api_Orders_blueprint = Blueprint('orders_api', __name__)

class OrderList(Resource):
    """ApiClass for get all orders list and add order"""
    def get(self) -> dict:
        """get all orders list"""
        response = get_all_orders()
        if response:
            return [json.loads(order.to_json()) for order in response]
        return {"description": "no orders"}

    def post(self) -> dict:
        """add order"""
        new_order = request.get_json(force=True)
        order = orders_schemas.CreateOrder(client_id=new_order.get('client_id'), room_id=new_order.get('room_id'),
                                        rented=new_order.get('rented'), renting_ends=new_order.get('renting_ends'))
        response = create_order(order)
        return response

class OrderListByClient(Resource):
    """ApiClass for searching order by client"""
    def post(self, client_id: int) -> list:
        """find order by client"""
        response = find_orders(client_id)
        return [json.loads(order.to_json()) for order in response]

class OrderDeleteUpdateAdd(Resource):
    """ApiClass for delete and put order"""
    def delete(self, order_id: int) -> dict:
        """delete order"""
        response = delete_order(order_id=order_id)
        return response

    def put(self, order_id: int) -> dict:
        """put order"""
        new_order_info = request.get_json(force=True)
        order = orders_schemas.EditOrder(id=order_id, client_id=new_order_info.get('client_id'),
                                          room_id=new_order_info.get('room_id'),
                                          rented=new_order_info.get('rented'),
                                          renting_ends=new_order_info.get('renting_ends'))
        response = edit_order(order=order)
        return json.loads(response.to_json())

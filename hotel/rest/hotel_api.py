from flask import Blueprint, json
from flask_restful import Resource, request
from hotel.service.hotel_crud import get_all_rooms, add_room, edit_room, delete_room, search_room_by_free_amount
from hotel.service.schemas import hotel_schemas
from typing import Union

api_Hotel_blueprint = Blueprint('hotel_api', __name__)

class HotelList(Resource):
    """ApiClass for get all rooms list and add room"""
    def get(self) -> list:
        """get all rooms list"""
        response = get_all_rooms()
        if response:
            return [json.loads(room.to_json()) for room in response]
        return {"description": "no rooms"}

    def post(self) -> dict:
        """add room"""
        new_room = request.get_json(force=True)
        room = hotel_schemas.AddRoom(area=new_room.get('area'),
                                     price_for_a_night=new_room.get('price_for_a_night'),
                                     max_amount_clients=new_room.get('max_amount_clients'))
        response = add_room(room)
        return response

class HotelListByFreeAmount(Resource):
    """ApiClass for searching free rooms"""
    def post(self, search_by_free_amount: int) -> Union[list, dict]:
        """get list of free rooms"""
        response = search_room_by_free_amount(search_by_free_amount)
        if response:
            return [json.loads(room.to_json()) for room in response]
        return {"description": "no rooms"}

class HotelDeleteUpdateAdd(Resource):
    """ApiClass for get all rooms list and add room"""
    def delete(self, room_id: int) -> dict:
        """delete room"""
        response = delete_room(room_id=room_id)
        return response

    def put(self, room_id: int) -> dict:
        """put room"""
        new_info_room = request.get_json(force=True)
        room = hotel_schemas.EditRoomInfo(id=room_id, area=new_info_room.get('area'),
                                          price_for_a_night=new_info_room.get('price_for_a_night'),
                                          max_amount_clients=new_info_room.get('max_amount_clients'))
        response = edit_room(room=room)
        return json.loads(response.to_json())

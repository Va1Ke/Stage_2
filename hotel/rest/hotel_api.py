from flask import Blueprint, json
from flask_restful import Resource, request
from hotel.service.hotel_crud import get_all_rooms, add_room, edit_room, delete_room, find_room
from hotel.service.schemas import hotel_schemas


api_Hotel_blueprint = Blueprint('hotel_api', __name__)

class HotelList(Resource):
    """ApiClass for get all rooms list and add room"""
    def get(self) -> list:
        """get all rooms list"""
        response = get_all_rooms()
        return [json.loads(room.to_json()) for room in response]

    def post(self) -> dict:
        """add room"""
        new_client = request.get_json(force=True)
        room = hotel_schemas.AddRoom(area=new_client.get('area'), number_of_beds=new_client.get('number_of_beds'),
                                     price_for_a_night=new_client.get('price_for_a_night'))
        response = add_room(room)
        return response

class HotelListByBusy(Resource):
    """ApiClass for showing list of free rooms"""
    def post(self, busy: int) -> list:
        """get list of free rooms"""
        response = find_room(busy)
        if type(response) == json:
            return response
        return [json.loads(room.to_json()) for room in response]

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
                                          number_of_beds=new_info_room.get('number_of_beds'),
                                          price_for_a_night=new_info_room.get('price_for_a_night'),
                                          busy=new_info_room.get('busy'))
        response = edit_room(room=room)
        return json.loads(response.to_json())

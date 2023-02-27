from flask import Blueprint
from flask_restful import reqparse, abort, Resource, request
from hotel.service.hotel_crud import get_all_rooms, add_room, edit_room, delete_room, find_room
from hotel.service.schemas import hotel_schemas
import json

api_Hotel_blueprint = Blueprint('hotel_api', __name__)

class HotelList(Resource):
    def get(self) -> list:
        response = get_all_rooms()
        return [json.loads(room.to_json()) for room in response]

    def post(self) -> dict:
        new_client = request.get_json(force=True)
        room = hotel_schemas.AddRoom(area=new_client.get('area'), number_of_beds=new_client.get('number_of_beds'),
                                     price_for_a_night=new_client.get('price_for_a_night'))
        response = add_room(room)
        return response

class HotelListByBusy(Resource):
    def post(self, busy: int) -> list:
        response = find_room(busy)
        if type(response) == json:
            return response
        return [json.loads(room.to_json()) for room in response]

class HotelDeleteUpdateAdd(Resource):

    def delete(self, room_id: int) -> dict:
        response = delete_room(room_id=room_id)
        return response

    def put(self, room_id: int) -> dict:
        new_info_room = request.get_json(force=True)
        room = hotel_schemas.EditRoomInfo(id=room_id, area=new_info_room.get('area'),
                                          number_of_beds=new_info_room.get('number_of_beds'),
                                          price_for_a_night=new_info_room.get('price_for_a_night'),
                                          busy=new_info_room.get('busy'))
        response = edit_room(room=room)
        return json.loads(response.to_json())



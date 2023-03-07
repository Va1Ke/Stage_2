import unittest
from hotel import create_app
from hotel.service.hotel_crud import get_all_rooms, search_room_by_free_amount, add_client_to_room, \
    subtract_client_from_room, update_rooms_amount, add_room, edit_room, delete_room
from hotel.service.clients_crud import get_all_clients
from hotel.service.schemas import hotel_schemas

class HotelServiceTestCase(unittest.TestCase):

    def test_get_all_rooms(self):
        with create_app().app_context():
            clients = get_all_rooms()
            self.assertEqual(True, isinstance(clients, list))
            self.assertIsNotNone(clients)

    def test_search_room_by_free_amount(self):
        with create_app().app_context():
            response = get_all_rooms()
            if len(response) > 0:
                client = search_room_by_free_amount(response[len(response)-1].free_amount)
                if len(client) > 0:
                    self.assertEqual(response[len(response)-1].free_amount, client[len(client)-1].free_amount)
                    self.assertIsNotNone(client)
                else:
                    self.assertEqual(True, isinstance(response, list))
            else:
                self.assertEqual(True, isinstance(response, list))

    def test_add_client_to_room(self):
        with create_app().app_context():
            clients = get_all_clients()
            if len(clients) > 0:
                rooms = get_all_rooms()
                if len(rooms) > 0:
                    response = add_client_to_room(rooms[len(rooms)-1].id)
                    if isinstance(response, dict) and "description" in response.keys():
                        self.assertEqual("Success", response["description"])
                        self.assertIsNotNone(response)
                    else:
                        self.assertEqual("no free amount in this room", response["description"])
                        self.assertIsNotNone(response)
                else:
                    self.assertEqual(True, isinstance(rooms, list))
            else:
                self.assertEqual(True, isinstance(clients, list))

    def test_subtract_client_from_room(self):
        with create_app().app_context():
            clients = get_all_clients()
            if len(clients) > 0:
                rooms = get_all_rooms()
                if len(rooms) > 0:
                    response = subtract_client_from_room(rooms[len(rooms)-1].id)
                    if isinstance(response, dict) and "description" in response.keys():
                        self.assertEqual("Success", response["description"])
                        self.assertIsNotNone(response)
                else:
                    self.assertEqual(True, isinstance(rooms, list))
            else:
                self.assertEqual(True, isinstance(clients, list))

    def test_update_rooms_amount(self):
        with create_app().app_context():
            response = update_rooms_amount()
            self.assertEqual("Success", response["description"])
            self.assertIsNotNone(response)

    def test_add_room(self):
        with create_app().app_context():
            new_room = hotel_schemas.AddRoom(area=25, price_for_a_night=32, max_amount_clients=3)
            response = add_room(new_room)
            self.assertEqual("Success", response["description"])
            self.assertIsNotNone(response)

    def test_edit_room(self):
        with create_app().app_context():
            rooms = get_all_rooms()
            if len(rooms) > 0:
                new_room_info = hotel_schemas.EditRoomInfo(id=rooms[len(rooms)-1].id, area=rooms[len(rooms)-1].area,
                                                           price_for_a_night=rooms[len(rooms)-1].price_for_a_night,
                                                           max_amount_clients=rooms[len(rooms)-1].max_amount_clients)
                response = edit_room(new_room_info)
                if isinstance(response, dict) and "description" in response.keys():
                    self.assertEqual("number_of_occupied must be <= than entered max_amount_clients",
                                     response["description"])
                    self.assertIsNotNone(response)
                self.assertEqual(new_room_info.area, response.area)
                self.assertEqual(new_room_info.price_for_a_night, response.price_for_a_night)
                self.assertEqual(new_room_info.max_amount_clients, response.max_amount_clients)
            else:
                self.assertEqual(True, isinstance(rooms, list))

    def test_delete_room(self):
        with create_app().app_context():
            response = get_all_rooms()
            if len(response) > 0:
                deleted = delete_room(response[len(response)-1].id)
                if isinstance(deleted, dict) and "description" in deleted.keys():
                    self.assertEqual("Success", deleted["description"])
                    self.assertIsNotNone(deleted)
                elif isinstance(deleted, dict) and "error" in deleted.keys():
                    self.assertEqual("room is busy", deleted["description"])
                    self.assertIsNotNone(deleted)
            else:
                self.assertEqual(True, isinstance(response, list))

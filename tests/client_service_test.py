import unittest
from hotel import create_app
from hotel.service.clients_crud import get_all_clients, find_client, add_client, edit_client, delete_client
from hotel.service.hotel_crud import get_all_rooms
from hotel.service.schemas import clients_schemas

class ClientServiceTestCase(unittest.TestCase):

    def test_get_all_clients(self):
        with create_app().app_context():
            clients = get_all_clients()
            self.assertEqual(True, isinstance(clients, list))
            self.assertIsNotNone(clients)

    def test_find_client(self):
        with create_app().app_context():
            response = get_all_clients()
            if len(response) > 0:
                client = find_client(response[len(response)-1].phone_number)
                self.assertEqual(response[len(response)-1].phone_number, client.phone_number)
                self.assertIsNotNone(client)
            else:
                self.assertEqual(True, isinstance(response, list))

    def test_add_client(self):
        with create_app().app_context():
            info = clients_schemas.AddClient(name="test", phone_number="+19823777")
            client = add_client(info)
            self.assertEqual(info.phone_number, client.phone_number)
            self.assertEqual(info.name, client.name)
            self.assertIsNotNone(client)

    def test_edit_client(self):
        with create_app().app_context():
            response = get_all_clients()
            if len(response) > 0:
                response_room = get_all_rooms()
                new_client_info = clients_schemas.EditClientInfo(id=response[len(response)-1].id,
                                                               name=response[len(response)-1].name,
                                                               phone_number=response[len(response)-1].phone_number,
                                                               room_id=response_room[len(response_room)-1].id)
                new_client = edit_client(new_client_info)
                self.assertEqual(new_client_info.phone_number, new_client.phone_number)
                self.assertEqual(new_client_info.name, new_client.name)
                self.assertEqual(new_client_info.room_id, new_client.room_id)
                self.assertIsNotNone(new_client)
            else:
                self.assertEqual(True, isinstance(response, list))

    def test_delete_client(self):
        with create_app().app_context():
            response = get_all_clients()
            if len(response) > 0:
                client = delete_client(response[len(response)-1].id)
                if isinstance(client, dict) and "description" in client.keys():
                    self.assertEqual("Success", client["description"])
                    self.assertIsNotNone(client)
            else:
                self.assertEqual(True, isinstance(response, list))

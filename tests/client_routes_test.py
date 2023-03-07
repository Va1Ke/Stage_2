import unittest
import requests
from hotel import create_app

class ClientServiceTestCase(unittest.TestCase):

    def test_get_list_clients(self):
        with create_app().app_context():
            response = requests.get('http://127.0.0.1:5000/client_list/')
            self.assertEquals(200, response.status_code)
            self.assertIsNotNone(response)

    def test_find_clients_by_phone_number(self):
        with create_app().app_context():
            response_get = requests.get('http://127.0.0.1:5000/clients/')
            if isinstance(response_get.json(), dict) and "description" in response_get.json().keys():
                self.assertEqual(response_get.json().get("description"), "no clients")
            else:
                data = {
                    'phone_number': response_get.json()[len(response_get.json())-1]["phone_number"]
                }
                response = requests.post('http://127.0.0.1:5000/client_list/', data=data)
                self.assertEquals(200, response.status_code)
                self.assertIsNotNone(response)

    def test_get_add_client_form(self):
        with create_app().app_context():
            response = requests.get('http://127.0.0.1:5000/client_list/add/')
            self.assertEquals(200, response.status_code)
            self.assertIsNotNone(response)

    def test_add_client(self):
        with create_app().app_context():
            data = {
                'name': 'test',
                'phone_number': "+298347293"
            }
            response = requests.post('http://127.0.0.1:5000/client_list/add/', data=data)
            self.assertEquals(200, response.status_code)
            self.assertIsNotNone(response)

    def test_get_edit_form(self):
        with create_app().app_context():
            response = requests.get('http://127.0.0.1:5000/client_list/edit/')
            self.assertEquals(200, response.status_code)
            self.assertIsNotNone(response)

    def test_edit_client(self):
        with create_app().app_context():
            response_get = requests.get('http://127.0.0.1:5000/clients/')
            if isinstance(response_get.json(), dict) and "description" in response_get.json().keys():
                self.assertEqual("no clients", response_get.json()["description"])
            else:
                response_get_rooms = requests.get('http://127.0.0.1:5000/rooms/')
                if isinstance(response_get_rooms.json(), dict) and "description" in response_get_rooms.json().keys():
                    self.assertEqual("no rooms", response_get_rooms.json()['description'])
                else:
                    data = {
                        'id': response_get.json()[len(response_get.json())-1]["id"],
                        'name': response_get.json()[len(response_get.json())-1]["name"],
                        'phone_number': response_get.json()[len(response_get.json())-1]["phone_number"],
                        'room_id': response_get_rooms.json()[len(response_get_rooms.json())-1]["room_id"]
                    }
                    response = requests.post('http://127.0.0.1:5000/client_list/edit/', data=data)
                    self.assertEquals(200, response.status_code)
                    self.assertIsNotNone(response)

    def test_get_delete_form(self):
        with create_app().app_context():
            response = requests.get('http://127.0.0.1:5000/client_list/delete/')
            self.assertEquals(200, response.status_code)
            self.assertIsNotNone(response)

    def test_delete_client(self):
        with create_app().app_context():
            response_get = requests.get('http://127.0.0.1:5000/clients/')
            if isinstance(response_get.json(), dict) and "description" in response_get.json().keys():
                self.assertEqual("no clients", response_get.json().get("description"))
            else:
                data = {
                    'id': response_get.json()[len(response_get.json())-1]["id"]
                }
                response = requests.post('http://127.0.0.1:5000/client_list/delete/', data=data)
                self.assertEquals(200, response.status_code)
                self.assertIsNotNone(response)

    def test_get_edit_form(self):
        with create_app().app_context():
            response = requests.get('http://127.0.0.1:5000/bad_request/')
            self.assertEquals(200, response.status_code)
            self.assertIsNotNone(response)

    def test_get_edit_form(self):
        with create_app().app_context():
            response = requests.get('http://127.0.0.1:5000/')
            self.assertEquals(200, response.status_code)
            self.assertIsNotNone(response)

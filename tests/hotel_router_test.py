import unittest
import requests
from hotel import create_app

class HotelServiceTestCase(unittest.TestCase):

    def test_get_list_room(self):
        with create_app().app_context():
            response = requests.get('http://127.0.0.1:5000/room_list/')
            self.assertEquals(200, response.status_code)
            self.assertIsNotNone(response)

    def test_find_free_rooms(self):
        with create_app().app_context():
            response = requests.get('http://127.0.0.1:5000/rooms/')
            if isinstance(response.json(), dict) and "description" in response.json().keys():
                self.assertEqual("no rooms", response.json()["description"])
            else:
                data = {
                    "search": response.json()[len(response.json())-1]["free_amount"]
                }
                response = requests.post('http://127.0.0.1:5000/room_list/', data=data)
                self.assertEquals(200, response.status_code)
                self.assertIsNotNone(response)

    def test_get_add_room_form(self):
        with create_app().app_context():
            response = requests.get('http://127.0.0.1:5000/room_list/add/')
            self.assertEquals(200, response.status_code)
            self.assertIsNotNone(response)

    def test_add_client(self):
        with create_app().app_context():
            area = 50
            data = {
                "area": area,
                "price_for_a_night": area+5,
                "max_amount_clients": 5,
            }
            response = requests.post('http://127.0.0.1:5000/room_list/add/', data=data)
            self.assertEquals(200, response.status_code)
            self.assertIsNotNone(response)

    def test_get_edit_form(self):
        with create_app().app_context():
            response = requests.get('http://127.0.0.1:5000/room_list/edit/')
            self.assertEquals(200, response.status_code)
            self.assertIsNotNone(response)

    def test_edit_room(self):
        with create_app().app_context():
            response_get = requests.get('http://127.0.0.1:5000/rooms/')
            if isinstance(response_get.json(), dict) and "description" in response_get.json().keys():
                self.assertEqual("no rooms", response_get.json()['description'])
            else:
                data = {
                    "id": response_get.json()[len(response_get.json())-1]["room_id"],
                    "area": 1,
                    "price_for_a_night": 1,
                    "max_amount_clients": 1
                }
                response = requests.post('http://127.0.0.1:5000/room_list/edit/', data=data)
                self.assertEquals(200, response.status_code)
                self.assertIsNotNone(response)

    def test_get_delete_form(self):
        with create_app().app_context():
            response = requests.get('http://127.0.0.1:5000/room_list/delete/')
            self.assertEquals(200, response.status_code)
            self.assertIsNotNone(response)

    def test_delete_client(self):
        with create_app().app_context():
            response_get = requests.get('http://127.0.0.1:5000/rooms/')
            if isinstance(response_get.json(), dict) and "description" in response_get.json().keys():
                self.assertEqual("no rooms", response_get.json().get("description"))
            else:
                data = {
                    'id': response_get.json()[len(response_get.json())-1]["room_id"]
                }
                response = requests.post('http://127.0.0.1:5000/room_list/delete/', data=data)
                self.assertEquals(200, response.status_code)
                self.assertIsNotNone(response)

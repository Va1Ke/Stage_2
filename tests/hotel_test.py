import unittest
import requests
import pytest

class HotelApiTestCase(unittest.TestCase):

    def test_create_room(self):
        response_all = requests.get("http://127.0.0.1:5000/rooms/")
        if isinstance(response_all.json(), dict) and "description" in response_all.json().keys():
            self.assertEqual(response_all.json().get("description"), "no rooms")
            amount_before = 0
        else:
            amount_before = len(response_all.json())
        var = amount_before + 1
        room_attrs = {
            "area": var,
            "number_of_beds": var,
            "price_for_a_night": var
        }
        response = requests.post("http://127.0.0.1:5000/rooms/", json=room_attrs)
        amount_after = len(requests.get("http://127.0.0.1:5000/rooms/").json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(amount_before + 1, amount_after)

    def test_get_all_rooms(self):
        response = requests.get("http://127.0.0.1:5000/rooms/")
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.json())

    def test_update_room(self):
        take_all = requests.get("http://127.0.0.1:5000/rooms/")
        if isinstance(take_all.json(), dict) and "description" in take_all.json().keys():
            self.assertEqual("no rooms", take_all.json().get('description'))
        else:
            var = len(take_all.json())
            room_attrs = {
                "area": var,
                "number_of_beds": var,
                "price_for_a_night": var,
                "busy": False
            }
            room_id = take_all.json()[len(take_all.json()) - 1].get('room_id')
            response = requests.put(f"http://127.0.0.1:5000/rooms/change/{room_id}", json=room_attrs)
            self.assertEqual(200, response.status_code)
            self.assertEqual(room_attrs['area'], response.json()['area'])
            self.assertEqual(room_attrs['number_of_beds'], response.json()['number_of_beds'])
            self.assertEqual(room_attrs['price_for_a_night'], response.json()['price_for_a_night'])

    def test_delete_room(self):
        take_all = requests.get("http://127.0.0.1:5000/rooms/")
        if isinstance(take_all.json(), dict) and "description" in take_all.json().keys():
            self.assertEqual("no rooms", take_all.json().get('description'))
        else:
            room_id = take_all.json()[len(take_all.json()) - 1].get('room_id')
            response = requests.delete(f"http://127.0.0.1:5000/rooms/change/{room_id}/")
            self.assertEqual(200, response.status_code)

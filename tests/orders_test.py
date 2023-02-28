import unittest
import requests


class OrderApiTestCase(unittest.TestCase):

    def test_create_order(self):
        amount_before = len(requests.get("http://127.0.0.1:5000/orders/").json())
        take_all_rooms = requests.get("http://127.0.0.1:5000/rooms/")
        take_all_clients = requests.get("http://127.0.0.1:5000/clients/")
        order_attrs = {
            "client_id": take_all_clients.json()[len(take_all_clients.json()) - 1].get('id'),
            "room_id": take_all_rooms.json()[len(take_all_rooms.json()) - 1].get('room_id'),
            "rented": "28/02/2023",
            "renting_ends": "02/03/2023"
        }
        response = requests.post("http://127.0.0.1:5000/orders/", json=order_attrs)
        amount_after = len(requests.get("http://127.0.0.1:5000/orders/").json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(amount_before + 1, amount_after)

    def test_get_all_order(self):
        response = requests.get("http://127.0.0.1:5000/orders/")
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.json())

    def test_update_order(self):
        take_all = requests.get("http://127.0.0.1:5000/orders/")
        take_all_rooms = requests.get("http://127.0.0.1:5000/rooms/")
        take_all_clients = requests.get("http://127.0.0.1:5000/clients/")
        var = len(take_all.json())
        order_attrs = {
            "client_id": take_all_clients.json()[len(take_all_clients.json()) - 1].get('id'),
            "room_id": take_all_rooms.json()[len(take_all_rooms.json()) - 1].get('room_id'),
            "rented": "25/02/2023",
            "renting_ends": "27/02/2023"
        }
        order_id = take_all.json()[len(take_all.json()) - 1].get('order_id')
        response = requests.put(f"http://127.0.0.1:5000/orders/change/{order_id}", json=order_attrs)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(order_attrs['client_id'], response.json()['client_id'])
        self.assertEqual(order_attrs['room_id'], response.json()['room_id'])
        self.assertEqual(order_attrs['rented'], response.json()['rented'])
        self.assertEqual(order_attrs['renting_ends'], response.json()['renting_ends'])

    def test_delete_order(self):
        take_all = requests.get("http://127.0.0.1:5000/orders/")
        room_id = take_all.json()[len(take_all.json()) - 1].get('order_id')
        response = requests.delete(f"http://127.0.0.1:5000/orders/change/{room_id}/")
        self.assertEqual(200, response.status_code)
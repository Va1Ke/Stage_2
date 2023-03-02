import unittest
import requests

class ClientApiTestCase(unittest.TestCase):

    def test_create_client(self):
        amount_before = len(requests.get("http://127.0.0.1:5000/clients/").json())
        var = amount_before + 1
        client_attrs = {
            "name": f"test{var}",
            "phone_number": f"phone_number{var}"
        }
        response = requests.post("http://127.0.0.1:5000/clients/", json=client_attrs)
        amount_after = len(requests.get("http://127.0.0.1:5000/clients/").json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(amount_before + 1, amount_after)

        response_take_all = requests.get("http://127.0.0.1:5000/clients/")
        new_in_db = response_take_all.json()[len(response_take_all.json()) - 1]
        self.assertEqual(new_in_db['name'], client_attrs['name'])
        self.assertEqual(new_in_db['phone_number'], client_attrs['phone_number'])

    def test_get_all_clients(self):
        response = requests.get("http://127.0.0.1:5000/clients/")
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.json())

    def test_update_client(self):
        take_all = requests.get("http://127.0.0.1:5000/clients/")
        if isinstance(take_all.json(), dict) and "description" in take_all.json().keys():
            self.assertEqual("no clients", take_all.json().get('description'))
        else:
            var = len(take_all.json())
            client_attrs = {
                "name": f"test{var}",
                "phone_number": f"phone_number{var}"
            }
            client_id = take_all.json()[len(take_all.json()) - 1].get('id')
            response = requests.put(f"http://127.0.0.1:5000/clients/change/{client_id}", json=client_attrs)
            print(response.status_code)
            self.assertEqual(200, response.status_code)
            self.assertEqual(client_attrs['name'], response.json()['name'])
            self.assertEqual(client_attrs['phone_number'], response.json()['phone_number'])

    def test_delete_client(self):
        take_all = requests.get("http://127.0.0.1:5000/clients/")
        if isinstance(take_all.json(), dict) and "description" in take_all.json().keys():
            self.assertEqual("no clients", take_all.json().get('description'))
        else:
            client_id = take_all.json()[len(take_all.json()) - 1].get('id')
            response = requests.delete(f"http://127.0.0.1:5000/clients/change/{client_id}")
            self.assertEqual(200, response.status_code)

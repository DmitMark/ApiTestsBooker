import requests
import json

class ApiBooker:

    def __init__(self):
        self.base_url = 'https://restful-booker.herokuapp.com'

    def create_token(self, username, password):

        headers = {'Content-Type': 'application/json'}

        data = {
            "username": username,
            "password": password

        }

        res = requests.post(self.base_url + '/auth', data=json.dumps(data), headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result




    def get_booking_ids(self, firstname= None, lastname= None, checkin= None, checkout= None):

        payload = {
            'firstname': firstname,
            'lastname': lastname,
            'checkin': checkin,
            'checkout': checkout
        }

        res = requests.get(self.base_url + '/booking', params=payload)

        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_booking(self, id):

        headers = {'Accept': 'application/json'}

        res = requests.get(self.base_url + '/booking/' + id, headers=headers)

        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def create_booking(self, firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds):

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        data = {
            "firstname": firstname,
            "lastname": lastname,
            "totalprice": totalprice,
            "depositpaid": depositpaid,
            "bookingdates": {
                "checkin": checkin,
                "checkout": checkout
            },
            "additionalneeds": additionalneeds
        }

        res = requests.post(self.base_url + '/booking', data=json.dumps(data), headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result




import requests
import json

class ApiBooker:

    def __init__(self):
        self.base_url = 'https://restful-booker.herokuapp.com'

    def create_token(self, payload):

        headers = {'Content-Type': 'application/json'}

        res = requests.post(self.base_url + '/auth',payload, headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result




    def get_booking_ids(self):

        res = requests.get(self.base_url+'/booking')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
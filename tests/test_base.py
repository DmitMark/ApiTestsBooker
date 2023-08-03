from api.api import ApiBooker
from serializers.booker import Token
from tests_data.tests_data import valid_username, valid_password
from api.payload import AuthorisePayload

book = ApiBooker()

auth_payload = AuthorisePayload('admin',
                                    'password123')

def test_create_token(payload = auth_payload):

    status, result = book.create_token(payload)

    print(result)
    assert status == 200
    assert 'token' is result

def test_get_booking_ids():

    status, result = book.get_booking_ids()

    assert status == 200
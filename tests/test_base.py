from api.api import ApiBooker
from serializers.booker import Token
from tests_data.tests_data import valid_username, valid_password, valid_firstname, valid_lastname, id, totalprice, depositpaid, valid_checkin, vakid_checkout, additionalneeds

book = ApiBooker()


def test_create_token(username = valid_username, password = valid_password):

    status, result = book.create_token(username, password)

    assert status == 200
    assert 'token' in result

def test_get_booking_ids():

    status, result = book.get_booking_ids()

    assert status == 200

def test_get_booking_ids_whith_name(firstname = valid_firstname, lastname = valid_lastname):

    status, result = book.get_booking_ids(firstname, lastname)

    assert status == 200

def test_get_booking_whith_id(id = id):

    status, result = book.get_booking(id)

    print(result)
    assert status == 200

def tests_create_booking(firstname = valid_firstname, lastname = valid_lastname, totalprice = totalprice, depositpaid = depositpaid, checkin = valid_checkin, checkout = vakid_checkout, additionalneeds = additionalneeds):

    status, result = book.create_booking(firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds)

    print(result)
    assert status == 200
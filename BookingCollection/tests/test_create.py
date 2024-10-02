from pytest_bdd import scenarios, given, when, then, parsers
import json
import requests
import pytest


scenarios("features/createbooking.feature")

passengerDetail = {
    "firstname": "Jim",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2024-07-08",
        "checkout": "2024-07-10"
    },
    "additionalneeds": "Breakfastt"
}

base_url='https://restful-booker.herokuapp.com/booking'


@pytest.fixture
def api_response():
    headers = {
        "Accept": "application/json",
        # Add other headers if necessary (e.g., Authorization)
    }
    response = requests.post(base_url,json=passengerDetail,headers=headers)
    return response


@when("the user create booking")
def create_booking(api_response):
     pass

@then(parsers.parse("the system responds with {status_code:d}"))
def system_responds_with_status_code(api_response, status_code):
    assert api_response.status_code == status_code, (
        f"Expected status code {status_code}, but got {api_response.status_code}"
    )

@then("the booking Id should be generated")
def assert_booking_id(api_response):
    assert "bookingid" in api_response.json()

@then("the booking details in the response should match the request")
def verify_booking_details(api_response):
    response_json = api_response.json()['booking']
    assert response_json['firstname'] == passengerDetail['firstname']
    assert response_json['lastname'] == passengerDetail['lastname']
    assert response_json['totalprice'] == passengerDetail['totalprice']
    assert response_json['depositpaid'] == passengerDetail['depositpaid']
    assert response_json['bookingdates']['checkin'] == passengerDetail['bookingdates']['checkin']
    assert response_json['bookingdates']['checkout'] == passengerDetail['bookingdates']['checkout']
    assert response_json['additionalneeds'] == passengerDetail['additionalneeds']
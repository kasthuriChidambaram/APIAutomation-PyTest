from pytest_bdd import scenarios, when, then, parsers
import requests
import pytest

# Feature file scenarios
scenarios("features/deletebooking.feature")

# Passenger details payload
passengerDetail = {
    "firstname": "Jim",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2024-07-08",
        "checkout": "2024-07-10"
    },
    "additionalneeds": "Breakfast"
}

# Base URL
base_url = 'https://restful-booker.herokuapp.com/booking'

# Fixture to create a booking
@pytest.fixture
def post_api_response():
    headers = {
        "Accept": "application/json",
    }
    response = requests.post(base_url, json=passengerDetail, headers=headers)
    return response

# Fixture to delete the booking
@pytest.fixture
def delete_api_response(post_api_response):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="  # Base64 encoded 'admin:password123'
    }
    bookingid = post_api_response.json()['bookingid']
    delete_url = f"{base_url}/{bookingid}"  # Embed bookingid into URL
    response = requests.delete(delete_url, headers=headers)
    return response

# Fixture to retrieve the booking details
@pytest.fixture
def get_api_response(post_api_response):
    headers = {
        "Accept": "application/json",
    }
    bookingid = post_api_response.json()['bookingid']
    get_url = f"{base_url}/{bookingid}"  # Embed bookingid into URL
    response = requests.get(get_url, headers=headers)
    return response

# Step to simulate booking creation
@when("the booking is created")
def create_booking(post_api_response):
    pass  # Booking is created via the post_api_response fixture

# Step to delete the booking
@when("the user deletes the booking with id")
def delete_booking(delete_api_response):
    pass  # Booking is deleted via the delete_api_response fixture

# Step to verify the system's response status code
@then(parsers.parse("the system responds with {status_code:d}"))
def system_responds_with_status_code(delete_api_response, status_code):
    assert delete_api_response.status_code == status_code, (
        f"Expected status code {status_code}, but got {delete_api_response.status_code}"
    )

# Step to verify the booking has been deleted
@then("the booking should be deleted")
def verify_booking_details(get_api_response):
    assert get_api_response.status_code == 404, (
        f"Expected status code 404 for deleted booking, but got {get_api_response.status_code}"
    )

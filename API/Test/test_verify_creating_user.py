from configuration import BASE_URL
import pytest
import requests

@pytest.fixture
def user_data():
    return {
        "id": 1,
        "username": "testuser123",
        "firstName": "John",
        "lastName": "Doe",
        "email": "john.doe@example.com",
        "password": "password123",
        "phone": "1234567890",
        "userStatus": 1
    }


def test_create_user(user_data):
    url = f'{BASE_URL}/user'
    response = requests.post(url, json=user_data)
    assert response.status_code == 200

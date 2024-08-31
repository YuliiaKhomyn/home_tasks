import time
import pytest
import requests
from configuration import BASE_URL

@pytest.fixture
def user_list():
    return [
        {
            "id": 2,
            "username": "user1_" + str(int(time.time())),
            "firstName": "Alice",
            "lastName": "Smith",
            "email": "alice.smith@example.com",
            "password": "password123",
            "phone": "1234567891",
            "userStatus": 1
        },
        {
            "id": 3,
            "username": "user2_" + str(int(time.time())),
            "firstName": "Bob",
            "lastName": "Jones",
            "email": "bob.jones@example.com",
            "password": "password123",
            "phone": "1234567892",
            "userStatus": 1
        }
    ]


def test_create_users(user_list):
    url = f'{BASE_URL}/user/createWithList'
    response = requests.post(url, json=user_list)
    assert response.status_code == 200


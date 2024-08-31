import pytest
import requests
from configuration import BASE_URL


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

def test_login_user(user_data):
    url = f'{BASE_URL}/user/login'
    response = requests.get(url, params={'username': user_data['username'], 'password': user_data['password']})
    assert response.status_code == 200
    assert 'logged in user session' in response.text
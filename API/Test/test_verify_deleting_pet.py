import pytest
import requests
from configuration import BASE_URL

@pytest.fixture
def pet_data():
    return {
        "id": 1,
        "category": {
            "id": 0,
            "name": "Dogs"
        },
        "name": "Buddy",
        "photoUrls": [
            "http://example.com/photo.jpg"
        ],
        "tags": [
            {
                "id": 1,
                "name": "friendly"
            }
        ],
        "status": "available"
    }


def test_delete_pet(pet_data):
    url = f'{BASE_URL}/pet'
    response = requests.post(url, json=pet_data)
    assert response.status_code == 200

    url = f'{BASE_URL}/pet/{pet_data["id"]}'
    response = requests.delete(url)
    assert response.status_code == 200
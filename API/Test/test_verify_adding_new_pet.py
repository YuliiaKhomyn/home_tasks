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


def test_add_pet(pet_data):
    url = f'{BASE_URL}/pet'
    response = requests.post(url, json=pet_data)

    # Check the response status code
    assert response.status_code == 200

    # Verify that the pet was added successfully
    response_data = response.json()
    assert response_data['name'] == pet_data['name']
    assert response_data['category'] == pet_data['category']
    assert response_data['photoUrls'] == pet_data['photoUrls']
    assert response_data['tags'] == pet_data['tags']
    assert response_data['status'] == pet_data['status']

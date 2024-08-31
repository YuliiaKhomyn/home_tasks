import requests
from configuration import BASE_URL

def test_update_pet_image():
    url = f'{BASE_URL}/pet'

    updated_pef_photo = {
        "id": 1,
        "photoUrls": [
            "http://example.com/photo1.jpg"
        ]
    }

    response = requests.put(url, json=updated_pef_photo)
    assert response.status_code == 200

    response_data = response.json()
    assert response_data['photoUrls'] == ['http://example.com/photo1.jpg']
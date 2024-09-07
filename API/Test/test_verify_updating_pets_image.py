import requests

from UI.Test.conftest import BASE_URL


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

    expected_url = ['http://example.com/photo1.jpg']
    actual_url = response_data['photoUrls']
    assert actual_url == expected_url, f"Expected url '{expected_url}' but got '{actual_url}'"

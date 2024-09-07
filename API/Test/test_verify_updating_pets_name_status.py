import requests
from UI.Test.conftest import BASE_URL

def test_update_pet_name_status():
    url = f'{BASE_URL}/pet'

    updated_json = {
        "id": 1,
        "name": "Buddy Updated",
        "status": "sold"
    }

    update_response = requests.put(url, json=updated_json)

    assert update_response.status_code == 200

    response_data = update_response.json()
    assert response_data['name'] == "Buddy Updated"
    assert response_data['status'] == "sold"

import pytest
import requests

from API.Test.constants import PET_DOG
from UI.Test.conftest import BASE_URL


@pytest.mark.parametrize("pet_data", [PET_DOG])
def test_add_pet(pet_data):
    url = f'{BASE_URL}/pet'
    response = requests.post(url, json=pet_data)

    assert response.status_code == 200

    response_data = response.json()
    assert response_data['name'] == pet_data['name'], f"Expected name '{pet_data['name']}' but got '{response_data['name']}'"
    assert response_data['category'] == pet_data['category'], f"Expected category '{pet_data['category']}' but got '{response_data['category']}'"
    assert response_data['photoUrls'] == pet_data['photoUrls'], f"Expected photo URLs '{pet_data['photoUrls']}' but got '{response_data['photoUrls']}'"
    assert response_data['tags'] == pet_data['tags'], f"Expected tags '{pet_data['tags']}' but got '{response_data['tags']}'"
    assert response_data['status'] == pet_data['status'], f"Expected status '{pet_data['status']}' but got '{response_data['status']}'"

import pytest
import requests

from API.Test.constants import PET_DOG
from UI.Test.conftest import BASE_URL


@pytest.mark.parametrize("pet_data", [PET_DOG])
def test_delete_pet(pet_data):
    url = f'{BASE_URL}/pet'
    response = requests.post(url, json=pet_data)
    assert response.status_code == 200

    url = f'{BASE_URL}/pet/{pet_data["id"]}'
    response = requests.delete(url)
    assert response.status_code == 200

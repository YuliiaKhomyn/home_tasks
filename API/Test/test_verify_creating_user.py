import pytest
import requests

from API.Test.constants import USER_DATA_1
from UI.Test.conftest import BASE_URL


@pytest.mark.parametrize("user_data", [USER_DATA_1])
def test_create_user(user_data):
    url = f'{BASE_URL}/user'
    response = requests.post(url, json=user_data)
    assert response.status_code == 200

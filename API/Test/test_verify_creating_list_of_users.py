import pytest
import requests

from API.Test.constants import USER_LIST
from UI.Test.conftest import BASE_URL


@pytest.mark.parametrize("user_list", [USER_LIST])
def test_create_users(user_list):
    url = f'{BASE_URL}/user/createWithList'
    response = requests.post(url, json=user_list)
    assert response.status_code == 200

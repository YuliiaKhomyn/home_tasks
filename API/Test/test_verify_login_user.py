import pytest
import requests

from API.Test.constants import USER_DATA_1
from UI.Test.conftest import BASE_URL


@pytest.mark.parametrize("user_data", [USER_DATA_1])
def test_login_user(user_data):
    url = f'{BASE_URL}/user/login'
    response = requests.get(url, params={'username': user_data['username'], 'password': user_data['password']})
    assert response.status_code == 200
    assert 'logged in user session' in response.text

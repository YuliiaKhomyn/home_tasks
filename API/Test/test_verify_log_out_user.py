import requests
from UI.Test.conftest import BASE_URL

def test_logout_user():
    logout_url = f'{BASE_URL}/user/logout'
    response = requests.get(logout_url)
    assert response.status_code == 200

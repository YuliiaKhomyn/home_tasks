from configuration import driver
from configuration import URL_CONTACT_US
from selenium.webdriver.common.by import By
import pytest



    #required_fields = [First Name, Last Name, Email, Phone, Location, How did you hear about EPAM? ]

@pytest.fixture(params=[
    {"email": "mailto:valid@example.com", "is_valid": "True"},
    {"email": "invalid@", "is_valid": "False"},
    {"email": "missing_at_example.com", "is_valid": "False"},
    {"email": "mailto:valid.email@example.com", "is_valid": "True"},
    {"email": "", "is_valid": "False"},
])
def email_test_data(request):
    return request.param

def test_email(driver, email_test_data):
    driver.get(URL_CONTACT_US)
    element = driver.find_element(By.CSS_SELECTOR,"[name='user_email']")
    email = email_test_data["email"]
    element.send_keys(email)
    expected = email_test_data["is_valid"]
    actual = element.get_attribute("aria-invalid")
    assert actual != expected


@pytest.fixture(params=[
    {"username": "mailto:valid@example.com", "is_valid": "True"},
    {"username": "invalid@", "is_valid": "True"},
    {"username": "missing_at_example.com", "is_valid": "True"},
    {"username": "mailto:valid.email@example.com", "is_valid": "True"},
    {"username": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "is_valid": "False"},
])
def username_test_data(request):
    return request.param

def test_username(driver, username_test_data):
    driver.get(URL_CONTACT_US)
    element = driver.find_element(By.CSS_SELECTOR,"[name='user_first_name']")
    username = username_test_data["username"]
    element.send_keys(username)
    expected = username_test_data["is_valid"]
    actual = element.get_attribute("aria-invalid")
    assert actual != expected

@pytest.fixture(params=[
    {"lastname": "mailto:valid@example.com", "is_valid": "True"},
    {"lastname": "invalid@", "is_valid": "True"},
    {"lastname": "missing_at_example.com", "is_valid": "True"},
    {"lastname": "mailto:valid.email@example.com", "is_valid": "True"},
    {"lastname": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "is_valid": "False"},
])
def last_name_test_data(request):
    return request.param

def test_last_name(driver, last_name_test_data):
    driver.get(URL_CONTACT_US)
    element = driver.find_element(By.CSS_SELECTOR,"[name='user_last_name']")
    lastname = last_name_test_data["lastname"]
    element.send_keys(lastname)
    expected = last_name_test_data["is_valid"]
    actual = element.get_attribute("aria-invalid")
    assert actual != expected


@pytest.fixture(params=[
    {"user_phone": "mailto:valid@example.com", "is_valid": "False"},
    {"user_phone": "1", "is_valid": "True"},
    {"user_phone": "-", "is_valid": "True"},
    {"user_phone": " ", "is_valid": "True"},
    {"user_phone": "1244545754", "is_valid": "True"},
    {"user_phone": ";", "is_valid": "False"}, #bug
    {"user_phone": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "is_valid": "False"},
    {"user_phone": "11111111111111111111111111111111111111111111111111111111111", "is_valid": "True"}, #bug
])
def user_phone_test_data(request):
    return request.param

def test_user_phone(driver, user_phone_test_data):
    driver.get(URL_CONTACT_US)
    element = driver.find_element(By.CSS_SELECTOR,"[name='user_phone']")
    user_phone = user_phone_test_data["user_phone"]
    element.send_keys(user_phone)
    expected = user_phone_test_data["is_valid"]
    actual = element.get_attribute("aria-invalid")
    assert actual != expected




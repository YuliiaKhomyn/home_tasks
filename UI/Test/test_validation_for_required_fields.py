import pytest
from selenium.webdriver.common.by import By

from UI.Test.conftest import URL_CONTACT_US
from UI.Test.conftest import driver
from UI.Test.constants import USER_PHONE_TEST_DATA, LAST_NAME_TEST_DATA, USERNAME_TEST_DATA, EMAIL_TEST_DATA


@pytest.mark.parametrize("email_test_data", EMAIL_TEST_DATA)
def test_email(driver, email_test_data):
    driver.get(URL_CONTACT_US)
    element = driver.find_element(By.CSS_SELECTOR, "[name='user_email']")
    email = email_test_data["email"]
    element.send_keys(email)
    expected = email_test_data["is_valid"]
    actual = element.get_attribute("aria-invalid")
    assert actual != expected


@pytest.mark.parametrize("username_test_data", USERNAME_TEST_DATA)
def test_username(driver, username_test_data):
    driver.get(URL_CONTACT_US)
    element = driver.find_element(By.CSS_SELECTOR, "[name='user_first_name']")
    username = username_test_data["username"]
    element.send_keys(username)
    expected = username_test_data["is_valid"]
    actual = element.get_attribute("aria-invalid")
    assert actual != expected


@pytest.mark.parametrize("last_name_test_data", LAST_NAME_TEST_DATA)
def test_last_name(driver, last_name_test_data):
    driver.get(URL_CONTACT_US)
    element = driver.find_element(By.CSS_SELECTOR, "[name='user_last_name']")
    lastname = last_name_test_data["lastname"]
    element.send_keys(lastname)
    expected = last_name_test_data["is_valid"]
    actual = element.get_attribute("aria-invalid")
    assert actual != expected


@pytest.mark.parametrize("user_phone, expected", USER_PHONE_TEST_DATA)
def test_user_phone(driver, user_phone, expected):
    driver.get(URL_CONTACT_US)
    element = driver.find_element(By.CSS_SELECTOR, "[name='user_phone']")
    element.send_keys(user_phone)
    actual = element.get_attribute("aria-invalid")
    assert actual != expected
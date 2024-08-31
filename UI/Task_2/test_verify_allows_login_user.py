import uuid

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from configuration import driver

def test_login_user(driver):
    driver.get('https://demowebshop.tricentis.com/')
    driver.find_element(By.LINK_TEXT, 'Log in').click()
    driver.find_element(By.ID, 'Email').send_keys('testuser11e0e9fa912c4bb6866c80a29563eaa8@example.com')
    driver.find_element(By.ID, 'Password').send_keys('Password123')
    driver.find_element(By.CSS_SELECTOR, 'input.button-1.login-button').click()
    welcome_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.header-links')))
    assert "Log out" in welcome_message.text

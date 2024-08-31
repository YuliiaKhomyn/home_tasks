import uuid

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from configuration import driver


def test_register_user(driver):
    driver.get('https://demowebshop.tricentis.com/')
    driver.find_element(By.LINK_TEXT, 'Register').click()
    driver.find_element(By.ID, 'gender-male').click()
    driver.find_element(By.ID, 'FirstName').send_keys('Test')
    driver.find_element(By.ID, 'LastName').send_keys('User')
    driver.find_element(By.ID, 'Email').send_keys(f"testuser{uuid.uuid4().hex}@example.com")
    driver.find_element(By.ID, 'Password').send_keys('Password123')
    driver.find_element(By.ID, 'ConfirmPassword').send_keys('Password123')
    driver.find_element(By.ID, 'register-button').click()
    success_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.result')))
    assert "Your registration completed" in success_message.text
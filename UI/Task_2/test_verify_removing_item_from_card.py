import uuid

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from configuration import driver

def test_remove_item_from_cart(driver):
    driver.get('https://demowebshop.tricentis.com/50s-rockabilly-polka-dot-top-jr-plus-size')

    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'add-to-cart-button-5'))
    )
    add_to_cart_button.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.bar-notification.success'))
    )

    driver.find_element(By.LINK_TEXT, 'Shopping cart').click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.cart'))
    )
    remove_checkbox = driver.find_element(By.NAME, 'removefromcart')
    remove_checkbox.click()

    update_cart_button = driver.find_element(By.NAME, 'updatecart')
    update_cart_button.click()

    cart_items = driver.find_elements(By.CSS_SELECTOR, '.cart-item-row')
    assert len(cart_items) == 0, "The item was not removed from the shopping cart."

    empty_cart_message = driver.find_element(By.CSS_SELECTOR, '.order-summary-content')
    assert "Your Shopping Cart is empty!" in empty_cart_message.text
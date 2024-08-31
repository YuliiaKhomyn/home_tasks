from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from configuration import driver

def test_add_item_to_cart(driver):
    driver.get('https://demowebshop.tricentis.com/50s-rockabilly-polka-dot-top-jr-plus-size')

    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'add-to-cart-button-5'))
    )

    add_to_cart_button.click()

    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.bar-notification.success'))
    )

    assert "The product has been added to your shopping cart" in success_message.text

    driver.find_element(By.LINK_TEXT, 'Shopping cart').click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.cart')))

    cart_items = driver.find_elements(By.CSS_SELECTOR, '.cart-item-row')
    assert len(cart_items) > 0, "No items found in the shopping cart."
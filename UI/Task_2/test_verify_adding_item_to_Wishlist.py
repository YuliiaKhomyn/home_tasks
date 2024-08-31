from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from configuration import driver

def test_add_item_to_wishlist(driver):
    driver.get('https://demowebshop.tricentis.com/50s-rockabilly-polka-dot-top-jr-plus-size')

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.item-box'))
    )

    first_item_wishlist_button = driver.find_element(By.CSS_SELECTOR, '.add-to-wishlist-button')
    first_item_wishlist_button.click()

    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.bar-notification.success'))
    )

    assert "The product has been added to your wishlist" in success_message.text

    driver.find_element(By.LINK_TEXT, 'Wishlist').click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.wishlist-content'))
    )
    product_price = driver.find_element(By.CSS_SELECTOR, ".product-subtotal").text
    assert product_price == '11.00'

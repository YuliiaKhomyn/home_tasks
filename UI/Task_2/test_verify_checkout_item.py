from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from configuration import driver

def test_checkout_item(driver):
    driver.get('https://demowebshop.tricentis.com/')
    driver.find_element(By.LINK_TEXT, 'Log in').click()
    driver.find_element(By.ID, 'Email').send_keys('testuser11e0e9fa912c4bb6866c80a29563eaa8@example.com')
    driver.find_element(By.ID, 'Password').send_keys('Password123')
    driver.find_element(By.CSS_SELECTOR, 'input.button-1.login-button').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.header-links')))

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
    driver.find_element(By.CSS_SELECTOR, ".terms-of-service").find_element(By.CSS_SELECTOR, "#termsofservice").click()

    checkout_button = driver.find_element(By.CSS_SELECTOR, '.checkout-button')
    checkout_button.click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.button-1.new-address-next-step-button'))).click()

    (WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout-step-shipping")))
     .find_element(By.CSS_SELECTOR, '.button-1.new-address-next-step-button').click())

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.button-1.shipping-method-next-step-button'))).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.button-1.payment-method-next-step-button'))).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.button-1.payment-info-next-step-button'))).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.button-1.confirm-order-next-step-button'))).click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.order-completed')))

    # Verify order completion
    order_confirmation_message = driver.find_element(By.CSS_SELECTOR, '.order-completed')
    assert "Your order has been successfully processed" in order_confirmation_message.text
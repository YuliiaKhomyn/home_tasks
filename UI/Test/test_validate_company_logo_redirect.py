from configuration import driver
from configuration import URL_ABOUT
from configuration import URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_validate_company_logo_redirect (driver):
    driver.get(URL_ABOUT)

    expected_link = URL

    logo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".header__logo-container")))
    logo.click()

    current_url_after_redirect = driver.current_url

    assert current_url_after_redirect == expected_link


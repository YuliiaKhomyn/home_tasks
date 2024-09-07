import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    height = 1080
    width = 1920

    if request.param == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)

    elif request.param == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(options=firefox_options)

    driver.set_window_size(width, height)

    yield driver

    driver.quit()

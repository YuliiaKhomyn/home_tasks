import pytest
from selenium import webdriver
import os
import tempfile

URL = "https://www.epam.com/"
URL_CONTACT_US = "https://www.epam.com/about/who-we-are/contact"
URL_ABOUT = "https://www.epam.com/about"
BASE_URL = "https://petstore.swagger.io/v2"


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    height = 1080
    width = 1920

    download_directory = os.path.join(tempfile.gettempdir(), "selenium_downloads")
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)

    if request.param == "chrome":
        chrome_options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": download_directory,
            "download.prompt_for_download": False,
            "directory_upgrade": True,
            "safebrowsing.enabled": True
        })

        driver = webdriver.Chrome(options=chrome_options)

    elif request.param == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        # options.add_argument("--headless")

        firefox_options.set_preference("browser.download.folderList", 2)
        firefox_options.set_preference("browser.download.dir", download_directory)
        firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk","application/pdf,application/octet-stream")
        firefox_options.set_preference("pdfjs.disabled", True)
        firefox_options.set_preference("browser.download.manager.showWhenStarting", False)
        firefox_options.set_preference("browser.download.panel.shown", False)

        driver = webdriver.Firefox(options=firefox_options)

    driver.set_window_size(width, height)

    yield driver

    driver.quit()

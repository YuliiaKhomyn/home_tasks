import os
import shutil
import tempfile

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from UI.Test.conftest import URL_ABOUT
from UI.Test.conftest import driver


def test_validate_download_report_name_extension(driver):
    driver.get(URL_ABOUT)

    buttons = driver.find_elements(By.CSS_SELECTOR, ".button-ui-23")
    download_directory = os.path.join(tempfile.gettempdir(), "selenium_downloads")

    try:
        for button in buttons:
            if button.text == 'DOWNLOAD':
                driver.execute_script("arguments[0].click();", button)
                break

        WebDriverWait(driver, 30).until(
            lambda d: any(fname.endswith('.pdf') for fname in os.listdir(download_directory))
        )

        files = [entry.name for entry in os.scandir(download_directory) if entry.is_file()]
        assert files[0] == "EPAM_Corporate_Overview_Q4_EOY.pdf"

    finally:
        if os.path.exists(download_directory):
            shutil.rmtree(download_directory)


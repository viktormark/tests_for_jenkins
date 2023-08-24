import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# docker exec -u 0 -it id /bin/bash
# chmod -x /usr/local/bin/chrome
# chmod -x /usr/local/bin/chromedriver


@pytest.fixture
def driver():
    options = Options()
    options.binary_location = '/usr/local/bin/chrome'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--verbose')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_add_remove_elements(driver):
    driver.get("http://the-internet.herokuapp.com/")
    driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[2]/a').click()

    driver.find_element(By.XPATH, '//*[@id="content"]/div/button').click()
    driver.find_element(By.XPATH, '//*[@id="content"]/div/button').click()

    buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")
    assert len(buttons) == 2

    buttons[0].click()
    buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")
    assert len(buttons) == 1

import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# @pytest.fixture
# def driver():
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.binary_location = '/usr/local/bin/chrome'
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     chrome_options.add_argument("--no-sandbox")
#
#     service = ChromeService(executable_path='/usr/local/bin/chromedriver')
#     driver = webdriver.Chrome(service=service, options=chrome_options)
#
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()



@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.binary_location = '/usr/local/bin/chrome'
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--verbose')
    driver = webdriver.Chrome(options=chrome_options)



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

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import pytest
from selenium.webdriver.support.wait import WebDriverWait
import time

@pytest.fixture(scope="class")
def setup(request):
    time.sleep(10)
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    #wait = WebDriverWait(driver , 100)
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    request.cls.driver = driver
    #request.cls.wait = wait

    yield
    request.cls.driver.close()


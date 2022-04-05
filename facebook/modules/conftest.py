from selenium import webdriver
from facebook.face_book_functions.configerations import Config
from pytest import fixture
@fixture
def _driver():
    driver = webdriver.Chrome(".\chromedriver.exe")
    driver.maximize_window()
    driver.get(Config.url)
    yield driver
    driver.quit()
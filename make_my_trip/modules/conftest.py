from selenium import webdriver
from make_my_trip.mmytrip.configerations import Config
from pytest import fixture
@fixture
def _driver():
    driver = webdriver.Chrome(".\chromedriver.exe")
    driver.maximize_window()
    driver.get(Config.url)
    yield driver
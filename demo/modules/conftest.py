from selenium import webdriver
from demo.functions.config import config
from pytest import fixture
"""fixtures are used to pass the data to test methods"""
"""or dependecy injection"""
@fixture
def _driver():
    driver = webdriver.Chrome("./chromedriver")
    # driver = webdriver.Chrome(r"C:\Users\Hp\PycharmProjects\kasi_selenium_train\kasi_sel_scen\chromedriver.exe")
    driver.get(config.URL)
    driver.maximize_window()
    yield driver
    driver.quit()

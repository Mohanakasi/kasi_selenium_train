from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from time import sleep
class Enable_check(visibility_of_element_located):
    def __call__(self, driver):
        displayed = super().__call__(driver)
        if isinstance(displayed, WebElement):
            return displayed.is_displayed()
        else:
            return False

def wait(func):
    def wrapper(*args, **kwargs):
        instance = args[0]
        locator_ = args[1]
        wait = WebDriverWait(instance.driver,50)
        v = Enable_check(locator_)
        wait.until(v)
        result = func(*args, **kwargs)
        sleep(5)
    return wrapper

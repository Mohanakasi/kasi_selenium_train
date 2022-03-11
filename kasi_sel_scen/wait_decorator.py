from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
class element_enable_check(visibility_of_element_located):
    def __call__(self, locat_):
        displayed = super().__call__(locat_)
        if isinstance(displayed, WebElement):
            return displayed.is_enabled()
        else:
            return False


def wait(func):
    def wrapper(*args, **kwargs):
        instance = args[0]
        locat_ = args[1]
        wait = WebDriverWait(instance.driver, 50)
        v = element_enable_check(locat_)
        wait.until(v)
        sleep(3)
        return func(*args, **kwargs)
    return wrapper

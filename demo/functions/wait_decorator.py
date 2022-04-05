from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement





class visibility_of_element_located(object):
    """ An expectation for checking that an element is present on the DOM of a
    page and visible. Visibility means that the element is not only displayed
    but also has a height and width that is greater than 0.
    locator - used to find the element
    returns the WebElement once it is located and visible
    """
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        try:
            return _element_if_visible(_find_element(driver, self.locator))
        except StaleElementReferenceException:
            return False
class element_enable_check(visibility_of_element_located):
    # def __init__(self,locator):
    #     self.loc = loc
    def __call__(self, driver):
        displayed = super().__call__(driver)
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

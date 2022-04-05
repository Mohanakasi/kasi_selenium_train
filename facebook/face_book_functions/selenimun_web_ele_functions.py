from selenium.webdriver.support.select import Select
from facebook.face_book_functions.wait_decorator_selenium import wait
from selenium.webdriver.common.action_chains import ActionChains
class Selenium_functions:
    def __init__(self, driver):
        self.driver = driver
    @wait
    def click_element(self, locator_):
        self.driver.find_element(*locator_).click()
    @wait
    def enter_text(self, locator_,value):
        self.driver.find_element(*locator_).send_keys(value)
    @wait
    def select_item_list_drop_down(self, locat_list_box, item):
        web_ele_list_box = self.driver.find_element(*locat_list_box)
        s = Select(web_ele_list_box)
        if isinstance(item, str):
            s.select_by_visible_text(item)
        elif isinstance(item, int):
            s.select_by_index(item)
        else:
            raise TypeError
    @wait
    def mouse_click(self, element):
        0

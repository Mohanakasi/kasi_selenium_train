from facebook.face_book_functions.selenimun_web_ele_functions import Selenium_functions
from selenium.webdriver.common.by import By
class Home_page_links(Selenium_functions):
    new_ac_link_web_el = (By.LINK_TEXT, "Create New Account")


    def __init__(self, driver):
        super().__init__(driver)

    def create_new_accounnt(self):
        self.click_element(self.new_ac_link_web_el)






from facebook.face_book_functions.selenimun_web_ele_functions import Selenium_functions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
class Login(Selenium_functions):
    un_web_el = (By.XPATH, "//input[@id='email']")
    pwd_web_el = (By.XPATH, "//input[@id='pass']")
    login_btn = (By.XPATH, "//button[text()='Log In']")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_user_name(self, un):
        self.enter_text(self.un_web_el, un)

    def enter_pass_word(self, pwd):
        self.enter_text(self.pwd_web_el, pwd)

    def click_login(self):
        self.click_element(self.login_btn)

    def notifi_pop(self):
        a1 = ActionChains(self.driver)
        a1.send_keys(Keys.ESCAPE)
        a1.send_keys(Keys.ESCAPE)


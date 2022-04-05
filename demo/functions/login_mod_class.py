from demo.functions.selenium_wrapper import selenium_functions
from selenium.webdriver.common.by import By
class Login_module(selenium_functions):
    un_web_el = (By.ID,"Email")
    pw_web_el = (By.ID,"Password")
    log_btn = (By.XPATH,"//input[@class='button-1 login-button']")
    def __init__(self,driver):
        super().__init__(driver)

    def enter_user_name(self,username):
        self.enter_text(self.un_web_el,username)

    def enter_password(self, password):
        self.enter_text(self.pw_web_el,password)

    def click_login_btn(self):
        self.click_elemet(self.log_btn)

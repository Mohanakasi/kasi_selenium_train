from demo.functions.selenium_wrapper import selenium_functions
from selenium.webdriver.common.by import By
class home_page_links(selenium_functions):
    register_web_ele = (By.XPATH,"//a[text()='Register']")
    login_web_el = (By.XPATH,"//a[text()='Log in']")
    books_web_el = (By.XPATH,"//a[@class='hover']")
    def __init__(self, driver):
        super().__init__(driver)
    def registration_page(self):
        self.click_elemet(self.register_web_ele)

    def login_page(self):
        self.click_elemet(self.login_web_el)

    def books_page(self):
        self.click_elemet(self.books_web_el)

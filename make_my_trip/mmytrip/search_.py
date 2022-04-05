from make_my_trip.mmytrip.selenimun_web_ele_functions import Selenium_functions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
class Search_bus(Selenium_functions):
    login_pop = (By.XPATH, "//li[@class='makeFlex hrtlCenter font10 makeRelative lhUser userLoggedOut']")
    add_close = (By.XPATH, "//span[@class='langCardClose']")
    bus_link = (By.XPATH, "//li[@class='menu_Buses']//a[@class='makeFlex hrtlCenter column']")
    from_city = (By.XPATH, "//label[@for='fromCity']")
    from_city_text = (By.XPATH, "//input[@placeholder='From']")
    to_city = (By.XPATH, "//label[@for='toCity']")
    to_city_text = (By.XPATH, "//input[@placeholder='To']")
    search_butt = (By.XPATH, "//button[@id='search_button']")
    bus_select = (By.XPATH, "//a[@class='sc-jKJlTe bPClQZ']")
    def __init__(self, driver):
        super().__init__(driver)

    def close_login_popup(self):
        self.click_element(self.login_pop)

    def ad_close(self):
        self.click_element(self.add_close)

    def click_on_bus(self):
        self.click_element(self.bus_link)

    def click_from_city(self):
        self.click_element(self.from_city)

    def enter_from_city(self, f_city):
        self.enter_text(self.from_city_text, f_city)
        sleep(4)
        self.click_element((By.XPATH, "//li[@id='react-autowhatever-1-section-0-item-0']"))

    def click_To_city(self):
        self.click_element(self.to_city)

    def enter_to_city(self, t_city):
        self.enter_text(self.to_city_text, t_city)
        sleep(4)
        self.click_element((By.XPATH, "//li[@id='react-autowhatever-1-section-0-item-0']"))

    def search_for_bus(self):
        self.click_element(self.search_butt)

    def select_date(self, month, date):
        i = 1
        while i > 0:
            try:
                m = self.driver.find_element(By.XPATH, f"//div[@class='bus_sw datePickerContainer']//div[text()='{month}']")
                day = self.driver.find_element(By.XPATH, f"//div[text()='{month}']/../..//div[text()='{date}']")
                day.click()
                break
            except NoSuchElementException:
                self.click_element((By.XPATH, "//span[@aria-label='Next Month']"))
                i += 1
    def select_the_bus(self):
        self.click_element(self.bus_select)

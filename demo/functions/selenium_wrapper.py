from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from demo.functions.wait_decorator import wait
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
class selenium_functions:
    def __init__(self,driver):
        self.driver = driver

    @wait
    def click_elemet(self,locat_): #locat_ ---> ("xpath","//span[text()='Sign in']")
        self.driver.find_element(*locat_).click() #*locat_--->"xpath","//span[text()='Sign in']"
        #driver.find_element("xpath","//span[text()='Sign in']").click()

    @wait
    def enter_text(self,locat_, value):
        self.driver.find_element(*locat_).send_keys(value)
    @wait
    def select(self,locat_, selecting_item):
        web_element = self.driver.find_element(*locat_)
        s = Select(web_element)
        if isinstance(selecting_item, str):
            s.select_by_visible_text(selecting_item)
        elif isinstance(selecting_item, int):
            s.select_by_index(selecting_item)
        else:
            raise TypeError


    def selec_check_boxes(self,list_names):
        for check_box_name in list_names:
            xpath_ = f"//td[text()='{check_box_name}']/..//input[@type='checkbox']"
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_xpath(xpath_).click()


    def select_item_list_box_dropdown(self,locator,selecting_item):
        s = Select(self.driver.find_element(*locator))
        s.select_by_visible_text(selecting_item)

    @wait
    def mouse_moove_to_element(self,locator):
        actions = ActionChains(self.driver)
        web_element = self.driver.find_element(*locator)
        actions.move_to_element(web_element).perform()

    # @wait
    # def date_picker(self,calender,month_year,date):
    #     try:
    #         self.driver.find_element(*calender)
    #         self.driver.find_element(*month_year)
    #         self.driver.find_element(*date).click()
    #     except NoSuchElementException:
            
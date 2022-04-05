from selenium.webdriver.common.by import By
from facebook.face_book_functions.selenimun_web_ele_functions import Selenium_functions
class Signup(Selenium_functions):
    first_name = (By.XPATH, "//div//input[@name='firstname']")
    last_name = (By.XPATH,"//div//input[@name='lastname']")
    mobile_num_email = (By.XPATH, "//div//input[@name='reg_email__']")
    confirm_mail = (By.XPATH, "//div[@class='uiStickyPlaceholderInput uiStickyPlaceholderEmptyInput']//input[@name='reg_email_confirmation__']")
    password = (By.XPATH, "//div[@class='uiStickyPlaceholderInput uiStickyPlaceholderEmptyInput']//input[@type='password']")
    dob_day = (By.XPATH,"//span//select[@aria-label='Day']")
    dob_month = (By.ID,"month")
    dob_year = (By.ID, "year")
    gender_male = (By.XPATH,"//span//label[text()='Male']")
    gender_female = (By.XPATH,"//span//label[text()='Female']")
    submit_butt = (By.XPATH,"//div[@class='_1lch']//button[text()='Sign Up']")
    def __init__(self,driver):
        super().__init__(driver)

    def enter_first_name(self, fname):
        self.enter_text(self.first_name, fname)

    def enter_last_name(self, lname):
        self.enter_text(self.last_name, lname)

    def enter_mobile_email(self, mobi_email):
        self.enter_text(self.mobile_num_email, mobi_email)

    def confirm_the_mail(self, mobi_email):
        self.enter_text(self.confirm_mail, mobi_email)

    def enter_password(self, pwd):
        self.enter_text(self.password, pwd)

    def enter_dob_day(self, day):
        self.select_item_list_drop_down(self.dob_day, day)

    def enter_dob_month(self, mon):
        self.select_item_list_drop_down(self.dob_month, mon)

    def enter_dob_year(self,year):
        self.select_item_list_drop_down(self.dob_year, year)

    def select_gender(self, gender):
        if gender.lower() == 'male':
            self.click_element(self.gender_male)
        elif gender.lower() == "female":
            self.click_element(self.gender_female)
        else:
            raise TypeError

    def submit_signup(self):
        self.click_element(self.submit_butt)

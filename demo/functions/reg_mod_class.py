from demo.functions.selenium_wrapper import selenium_functions
class Regitration_(selenium_functions):
    _gender_male = ("id","gender-male")
    _gender_female = ("id","gender-female")
    _fname = ("id","FirstName")
    _lname  = ("id","LastName")
    _email = ("name","Email")
    _password = ("id","Password")
    _confpassword = ("id","ConfirmPassword")
    _reg_btn = ("id","register-button")
    _reg_continue = ("xpath","//div[@class='center-2']//input[@class='button-1 register-continue-button']")
    def __init__(self, driver):
        super().__init__(driver)

    def select_gender_male(self):
        self.click_elemet(self._gender_male)

    def select_gender_female(self):
        self.click_elemet(self._gender_female)

    def enter_first_name(self,fname):
        self.enter_text(self._fname,fname)

    def enter_last_name(self,lname):
        self.enter_text(self._lname,lname)

    def enter_email(self, email):
        self.enter_text(self._email,email)

    def enter_password(self, password):
        self.enter_text(self._password, password)

    def enter_confirm_password(self, cnfpassword):
        self.enter_text(self._confpassword, cnfpassword)


    def click_regis_button(self):
        self.click_elemet(self._reg_btn)

    def click_continue(self):
        self.click_elemet(self._reg_continue)

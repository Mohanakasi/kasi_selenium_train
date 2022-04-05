from demo.functions.home_page import home_page_links
from demo.functions.reg_mod_class import Regitration_
from pytest import mark
header = ["gender","fname","lname","email","password","confirm_password",]
data = [("male","mohana kasi","settipalli","mohana7896@gmail.com","Mohana21995","Mohana21995")]
@mark.parametrize(header,data)
def test_register(_driver,gender,fname,lname,email,password,confirm_password):
    hp = home_page_links(_driver)
    hp.registration_page()
    reg = Regitration_(_driver)
    if gender == "male":
        reg.select_gender_male()
    elif gender == 'female':
        reg.select_gender_female()
    reg.enter_first_name(fname)
    reg.enter_last_name(lname)
    reg.enter_email(email)
    reg.enter_password(password)
    reg.enter_confirm_password(confirm_password)
    reg.click_regis_button()
    reg.click_continue()



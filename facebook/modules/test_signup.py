from facebook.face_book_functions.signup_modu_class import Signup
from pytest import mark
from facebook.face_book_functions.home_page_links import Home_page_links
header = ["first_name","last_name","mobile_or_email","password","day","month","year","gender"]
data = [("Mohana kasi","settipalli","kasi.jmr@gmail.com","Mohana@1995","14","Dec","1995","male")]
@mark.parametrize(header,data)
def test_signup(_driver, first_name, last_name, mobile_or_email, password, day, month, year,gender):
    hp = Home_page_links(_driver)
    hp.create_new_accounnt()
    si = Signup(_driver)
    si.enter_first_name(first_name)
    si.enter_last_name(last_name)
    si.enter_mobile_email(mobile_or_email)
    si.confirm_the_mail(mobile_or_email)
    si.enter_password(password)
    si.enter_dob_day(day)
    si.enter_dob_month(month)
    si.enter_dob_year(year)
    si.select_gender(gender)
    si.submit_signup()





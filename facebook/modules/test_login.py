from facebook.face_book_functions.login_mod_class import Login
from time import sleep
from pytest import mark
header = ["user_name","password"]
data = [(8886213059,"Robo@1995")]
@mark.parametrize(header,data)
def test_login_case(_driver,user_name, password):
    l1 = Login(_driver)
    l1.enter_user_name(user_name)
    l1.enter_pass_word(password)
    l1.click_login()
from demo.functions.home_page import home_page_links
from demo.functions.login_mod_class import Login_module
from pytest import mark
header = ["user_name","password"]
data = [("mohana7896@gmail.com","Mohana21995")]
@mark.parametrize(header,data)
def test_login_page(_driver, user_name,password):
    login_link_obj = home_page_links(_driver)
    login_link_obj.login_page()
    lp = Login_module(_driver)
    lp.enter_user_name(user_name)
    lp.enter_password(password)
    lp.click_login_btn()



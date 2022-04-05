# class temp:
#     count = 0
#     def __init__(self):
#         temp.count +=1
#
# a = temp()
# b = temp()
# c = temp()
# print(temp.count)


# class Samp:
#     def __init__(self, item):
#         self.item = item
#
#     def __iter__(self):
#         return iter(self.item)
#
# s = Samp([1,2,3])
# for item in s:
#     print(item)

from selenium.webdriver.support.color import Color
# HEX_COLOUR = Color.from_string('#2F7ED8')
# print(HEX_COLOUR)
# Black_ = Color.from_string("black")
# print(Black_)
#
# hex_ = Color.from_string("#fff")
# print(hex_)


from selenium import webdriver
driver = webdriver.Chrome(".\chromedriver.exe")
# # driver.get("https://www.makemytrip.com/")
# # search_button = Color.from_string("blue")
# # search_butt_color = Color.from_string(driver.find_element_by_xpath("//a[text()='Search']").value_of_css_property('color'))
# # print(search_button)
# # print(search_butt_color.hex)
# # assert search_butt_color.rgba == 'rgba(255, 255, 255, 1)'
# # assert search_butt_color.hex == '#fff'
#
#
# # driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
# # but_color = Color.from_string(driver.find_element_by_xpath("//span[@id='continue']").value_of_css_property('color'))
# # print(but_color)
# # print(but_color.hex)
#
#
# driver.get("http://demowebshop.tricentis.com/notebooks")
# reg_but_web_el = driver.find_element_by_xpath("//a[text()='Register']")
#
# reg_but_color = Color.from_string(reg_but_web_el.value_of_css_property('color'))
# # print(reg_but_color.hex)
# print(reg_but_color.hex.upper())
# assert reg_but_color.hex.upper() == "#AF0304"
#
# add_to_cart_el = driver.find_element_by_xpath("//input[@class='button-2 product-box-add-to-cart-button']")
# cart_color = Color.from_string(add_to_cart_el.value_of_css_property('color'))
# print(cart_color.hex)

# from requests import request
# print(request("Get","http://demowebshop.tricentis.com/notebooks"))

driver.get("http://demowebshop.tricentis.com/notebooks")
laptop_img = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[3]/div/div/div[1]/a/img")
print(laptop_img.is_displayed())
book
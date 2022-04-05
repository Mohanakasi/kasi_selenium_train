# import xlrd
# path = r'D:\temp_login_reading.xlsx'
# new_book = xlrd.open_workbook(path)
# new_sheet = new_book.sheet_by_name(r"login_data")
# rows = new_sheet.get_rows()
# next(rows)
# d = {}
# for row in rows:
#     print(row)
#     d[row[0].value] = (row[1].value, row[2].value)
# print(d)

# class temp_:
#     def __init__(self):
#         print("hai")
#
#     def display():
#         print("hello")
# a = temp_()
# a.display()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(r"C:\Users\Hp\PycharmProjects\kasi_selenium_train\kasi_sel_scen\chromedriver.exe")
driver.get(r"https://www.google.com/")
driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").send_keys("shruthi testyantra", Keys.ENTER)
a = ActionChains(driver)
a.send_keys(Keys.PAGE).perform()

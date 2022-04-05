from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
driver = webdriver.Chrome("./chromedriver")

class enable_check(visibility_of_element_located):



wait = WebDriverWait(driver,50)
v = visibility_of_element_located(("link_text","Register"))
wait.until(v)


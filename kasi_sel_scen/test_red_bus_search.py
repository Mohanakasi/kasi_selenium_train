from selenium import webdriver
from kasi_sel_scen.selenium_wrapper import selenium_functions
from kasi_sel_scen.config import config
from selenium.webdriver.common.by import By
def test_red_bus(_driver):
    s = selenium_functions(_driver)
    s.enter_text((By.ID,"src"),"guntur")
    s.enter_text((By.ID,"dest"),"bangalore")
    s.click_elemet((By.XPATH,"//div[@class='fl search-box date-box gtm-onwardCalendar']//span[@class='fl icon-calendar_icon-new icon-onward-calendar icon']"))
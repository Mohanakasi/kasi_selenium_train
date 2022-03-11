from selenium import webdriver
from selenium.webdriver.common.by import By
from kasi_sel_scen.selenium_wrapper import selenium_functions
from time import sleep
from kasi_sel_scen.config import config

def test_logn():
    driver = webdriver.Chrome()
    driver.get(config.URL)
    driver.maximize_window()
    s = selenium_functions(driver)
    s.mouse_moove_to_element((By.XPATH,"//a[@id='nav-link-accountList']"))
    s.click_elemet((By.XPATH,"//span[text()='Sign in']"))
    s.enter_text((By.XPATH,"//input[@id='ap_email']"),config.USER_NAME)
    s.click_elemet((By.XPATH,"//input[@id='continue']"))
    s.enter_text((By.XPATH,"//input[@id='ap_password']"),config.PASSWORD)
    s.click_elemet((By.XPATH,"//input[@id='signInSubmit']"))




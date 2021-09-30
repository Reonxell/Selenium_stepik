from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
WebDriverWait(driver, 5).until(text_to_be_present_in_element((By.ID, 'sadas'), 'dsadsaasdsad'))
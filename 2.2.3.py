from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()

link = 'http://suninjuly.github.io/selects1.html'

browser.get(link)
a = browser.find_element_by_css_selector('h2 #num1').text
b = browser.find_element_by_css_selector('h2 #num2').text
rez = int(a) + int(b)
Select(browser.find_element_by_css_selector('select#dropdown')).select_by_value(str(rez))
browser.find_element_by_css_selector('button').click()
time(30)
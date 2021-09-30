import time

from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)
x = browser.find_element_by_css_selector('#input_value').text
x = calc(int(x))
browser.find_element_by_css_selector('#answer').send_keys(x)
browser.find_element_by_css_selector('#robotCheckbox').location_once_scrolled_into_view
browser.find_element_by_css_selector('#robotCheckbox').click()
browser.find_element_by_css_selector('#robotsRule').click()
browser.find_element_by_css_selector('button').click()
time.sleep(30)

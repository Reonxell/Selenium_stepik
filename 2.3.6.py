import pytest
from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

link = 'http://suninjuly.github.io/redirect_accept.html'

browser.get(link)
browser.find_element_by_css_selector('button.trollface').click()
browser.switch_to.window(browser.window_handles[1])
x = browser.find_element_by_css_selector('#input_value').text
x = calc(x)
browser.find_element_by_css_selector('input.form-control').send_keys(x)
browser.find_element_by_css_selector('button').click()

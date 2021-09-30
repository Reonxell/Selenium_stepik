import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.ui import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

link = 'http://suninjuly.github.io/explicit_wait2.html'

browser.get(link)
WebDriverWait(browser, 12).until(text_to_be_present_in_element((By.ID, 'price'), '$100'))
browser.find_element_by_id('book').click()
browser.find_element_by_css_selector('#input_value').location_once_scrolled_into_view
x = browser.find_element_by_css_selector('#input_value').text
x =calc(x)
browser.find_element_by_id('answer').send_keys(x)
browser.find_element_by_css_selector('#solve').click()



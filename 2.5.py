from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/math.html'
browser.get(link)
x = browser.find_element_by_css_selector('.container .nowrap#input_value').text
x = calc(x)
browser.find_element_by_css_selector('.form-group #answer').send_keys(x)
browser.find_element_by_css_selector('.form-check #robotCheckbox').click()
browser.find_element_by_css_selector('.form-radio-custom #robotsRule').click()
browser.find_element_by_css_selector('button.btn-default').click()

time.sleep(30)


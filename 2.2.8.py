from selenium import webdriver
import os.path

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'
browser.get(link)
browser.find_element_by_css_selector('input.form-control[name="firstname"]').send_keys('1')
browser.find_element_by_css_selector('input.form-control[name="lastname"]').send_keys('2')
browser.find_element_by_css_selector('input.form-control[name="email"]').send_keys('3')
path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '1.txt')
browser.find_element_by_css_selector('#file').send_keys(path)
browser.find_element_by_css_selector('button').click()
browser.switch_to_alert()

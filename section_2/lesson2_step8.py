import os
from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    #filling in all text fields
    names = ["firstname", "lastname", "email"]
    for name in names:
        browser.find_element_by_name(name).send_keys("something")

    #attaching file
    file_name = "test.txt"
    dir_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(dir_path, file_name)
    browser.find_element_by_id("file").send_keys(file_path)

    #sending form
    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(5)
    browser.quit()

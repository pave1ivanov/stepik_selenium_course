from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    browser.find_element_by_css_selector("button.trollface").click()
    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element_by_id("input_value").text
    result = calc(x)
    browser.find_element_by_id("answer").send_keys(result)
    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(5)
    browser.quit()

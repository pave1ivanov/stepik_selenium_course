from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("input_value").text
    restult = calc(x)

    browser.find_element_by_id("answer").send_keys(restult)
    browser.find_element_by_css_selector("[for='robotCheckbox']").click()
    browser.find_element_by_css_selector("[for='robotsRule']").click()
    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(5)
    browser.quit()

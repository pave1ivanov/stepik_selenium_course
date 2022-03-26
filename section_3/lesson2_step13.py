from selenium import webdriver
import unittest
import time

class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        required_placeholders = ['first', 'last', 'email']
        for x in required_placeholders:
            browser.find_element_by_css_selector("input[placeholder~='" + x + "']").send_keys('Something')
        
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Registration failed")
        browser.quit()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        required_placeholders = ['first', 'last', 'email']
        for x in required_placeholders:
            browser.find_element_by_css_selector("input[placeholder~='" + x + "']").send_keys('Something')
        
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Registration failed")
        browser.quit()

if __name__ == "__main__":
    unittest.main()

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math
import pytest

link_list = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
    ]
expected_text = "Correct!"

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.mark.parametrize('link', link_list)
def test_stepik_optional_feedback(browser, link):
    browser.get(link)
    
    input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ember-text-area"))
    )
    input.send_keys(str(math.log(int(time.time()))))

    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    )
    button.click()

    text = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
    ).text

    assert text == expected_text, "Feedback is not as expected"

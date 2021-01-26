import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    time.sleep(2)
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('num', ["236895", "236896", "236897", "236898", "236899",
                                 "236903", "236904", "236905"])
def test_stepik_input(browser, num):
    link = f"https://stepik.org/lesson/{num}/step/1/"
    browser.get(link)
    browser.implicitly_wait(3)
    answer = math.log(int(time.time()))
    text1 = browser.find_element_by_tag_name("textarea")
    text1.send_keys(str(answer))
    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()

    text_el = browser.find_element_by_css_selector(".smart-hints__hint")
    assert "Correct!" == text_el.text, "NOT CORRECT!"


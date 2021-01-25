from selenium import webdriver
import time
import unittest


# Ваш код, который заполняет обязательные поля
class Test_stepik(unittest.TestCase):
    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        elements = browser.find_element_by_css_selector(".first_block input.form-control.first")
        elements.send_keys("Мой ответ")
        elements = browser.find_element_by_css_selector(".first_block input.form-control.second")
        elements.send_keys("Мой ответ")
        elements = browser.find_element_by_css_selector(".first_block input.form-control.third")
        elements.send_keys("Мой ответ")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        elements = browser.find_element_by_css_selector(".first_block input.form-control.first")
        elements.send_keys("Мой ответ")
        elements = browser.find_element_by_css_selector(".first_block input.form-control.second")
        elements.send_keys("Мой ответ")
        elements = browser.find_element_by_css_selector(".first_block input.form-control.third")
        elements.send_keys("Мой ответ")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        # self.assertEqual(test_1, test_2)


if __name__ == "__main__":
    unittest.main()
    print("Everything passed")

    # Отправляем заполненную форму
# ожидание чтобы визуально оценить результаты прохождения скрипта
# time.sleep(2)
# закрываем браузер после всех манипуляций
# browser.quit()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
# time.sleep(5)

# находим элемент, содержащий текст
# welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
# welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
# assert "Congratulations! You have successfully registered!" == welcome_text


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestURL(unittest.TestCase):
    def test1(self):
        try:
            link = "https://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            #Обязательные полня
            input_first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
            input_first_name.send_keys("Andrey")

            input_last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
            input_last_name.send_keys("Alexsandrov")

            input_email = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
            input_email.send_keys("test@mail.ru")

            #Отправка формы с обязательными полями
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            #Проверяем что мы зарегались
            #ждем загрузку старницы
            time.sleep(1)

            #находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            #проверяем с assert
            assert "Congratulations! You have successfully registered!" == welcome_text


        finally:
            time.sleep(10)
            browser.quit()

    def test2(self):
        try:
            link = "https://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            #Обязательные полня
            input_first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
            input_first_name.send_keys("Andrey")

            input_last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
            input_last_name.send_keys("Alexsandrov")

            input_email = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
            input_email.send_keys("test@mail.ru")

            #Отправка формы с обязательными полями
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            #Проверяем что мы зарегались
            #ждем загрузку старницы
            time.sleep(1)

            #находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            #проверяем с assert
            assert "Congratulations! You have successfully registered!" == welcome_text


        finally:
            time.sleep(10)
            browser.quit()

if __name__ == "__main__":
    unittest.main()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/huge_form.html")

    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("Тест")

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(30)
    browser.quit()


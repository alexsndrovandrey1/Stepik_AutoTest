from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    a = str(math.ceil(math.pow(math.pi, math.e)*10000))
    print(a)
    link1 = browser.find_element(By.LINK_TEXT, a)
    link1.click()

    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Andrey")

    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Alexsandrov")

    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Moscow")

    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()


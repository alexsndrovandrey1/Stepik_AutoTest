from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math

def sum(a,b):
    return (str(str(int(a)+int(b))))

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.CSS_SELECTOR, ".nowrap#num1")
    a = num1.text

    num2 = browser.find_element(By.CSS_SELECTOR, ".nowrap#num2")
    b = num2.text

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum(a,b)))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

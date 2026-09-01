from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    img = browser.find_element(By.ID, "treasure")
    x = img.get_attribute("valuex")

    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    check_box = browser.find_element(By.ID, "robotCheckbox")
    check_box.click()

    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    submit_btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_btn.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()

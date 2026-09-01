from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    house_price =  WebDriverWait(browser, 12).until(
       EC.text_to_be_present_in_element((By.ID, "price"), "$100"))


    button = browser.find_element(By.ID, "book")
    button.click()

    x_elememt = browser.find_element(By.ID, "input_value")
    x =  x_elememt.text
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    submit_btn = browser.find_element(By.ID, "solve")
    submit_btn.click()


finally:
    time.sleep(10)
    browser.quit()

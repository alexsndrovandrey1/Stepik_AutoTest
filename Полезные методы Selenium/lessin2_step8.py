from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    fname = browser.find_element(By.NAME, "firstname")
    fname.send_keys("Andrey")

    lname = browser.find_element(By.NAME, "lastname")
    lname.send_keys("Alexsandrov")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("an.alex25@mail.ru")

    current_path_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_path_dir, "test.txt")

    download_file = browser.find_element(By.CSS_SELECTOR, "input#file")
    download_file.click()
    download_file.send_keys(file_path)

    sub_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    sub_button.click()

finally:
    time.sleep(10)
    browser.quit()
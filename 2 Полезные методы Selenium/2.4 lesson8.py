from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открыть сайт в браузере
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ожидание не менее 12 секунд, пока цена не понизится до 100 долларов
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    # Нажимаем кнопку
    btn = browser.find_element(By.ID, "book")
    btn.click()

    # Решаем функцию, вставляем решение в поле
    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    y = calc(x)
    input = browser.find_element(By.CSS_SELECTOR, "[name='text']")
    input.send_keys(y)

    # Нажимаем кнопку
    submit = browser.find_element(By.CSS_SELECTOR, "[type= 'submit']")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

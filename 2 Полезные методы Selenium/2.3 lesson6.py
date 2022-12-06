from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  #Открыть сайт в браузере
  link = "http://suninjuly.github.io/redirect_accept.html"
  browser = webdriver.Chrome()
  browser.get(link)

  # Нажимаем кнопку
  btn = browser.find_element(By.TAG_NAME, "button")
  btn.click()

  #Переходим на новую вкладку
  new_window = browser.window_handles[1]
  browser.switch_to.window(new_window)
  
  #Решаем функцию, вставляем решение в поле
  x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
  x = x_element.text
  y = calc(x)
  input = browser.find_element(By.CSS_SELECTOR, "[name='text']")
  input.send_keys(y)

  #Нажимаем кнопку
  submit = browser.find_element(By.CSS_SELECTOR, "[type= 'submit']")
  submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

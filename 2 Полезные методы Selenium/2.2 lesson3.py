from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import math

def sum(x, y):
  return str(int(x) + int(y))

try:
  #Открыть сайт в браузере
  link = "http://suninjuly.github.io/selects1.html"
  browser = webdriver.Chrome()
  browser.get(link)

  #Считать значение переменной X и подставить его в функцию
  x_element = browser.find_element(By.CSS_SELECTOR, "[id='num1']")
  x = x_element.text
  y_element = browser.find_element(By.CSS_SELECTOR, "[id='num2']")
  y = y_element.text
  sum_el = sum(x, y)

  select = Select(browser.find_element(By.TAG_NAME, "select"))
  select.select_by_value(str(sum_el))

  #Нажать кнопку
  submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
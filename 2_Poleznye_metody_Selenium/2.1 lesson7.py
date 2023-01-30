from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  #Открыть сайт в браузере
  link = "http://suninjuly.github.io/get_attribute.html"
  browser = webdriver.Chrome()
  browser.get(link)

  #Считать значение переменной X и подставить его в функцию
  x_element = browser.find_element(By.ID, "treasure")
  x = x_element.get_attribute("valuex")
  #x = valuex
  y = calc(x)

  #Результат вводим в текстовое поле
  input = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
  input.send_keys(y)

  #Отметить чекбокс, выбрать радиобаттон, нажать кнопку
  checkbox = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
  checkbox.click()
  radiobutton = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
  radiobutton.click()
  submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
  submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
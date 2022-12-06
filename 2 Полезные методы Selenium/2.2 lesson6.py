from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  #Открыть сайт в браузере
  link = "http://suninjuly.github.io/execute_script.html"
  browser = webdriver.Chrome()
  browser.get(link)

  #Считать значение переменной X и подставить его в функцию
  x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
  x = x_element.text
  y = calc(x)

  #Результат вводим в текстовое поле
  input = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
  input.send_keys(y)

  #Скроллинг страницы вниз
  button = browser.find_element(By.TAG_NAME, "button")
  browser.execute_script("return arguments[0].scrollIntoView(true);", button)

  #Отметить чекбокс, выбрать радиобаттон, нажать кнопку
  checkbox = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
  checkbox.click()
  radiobutton = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
  radiobutton.click()
  time.sleep(1)
  button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
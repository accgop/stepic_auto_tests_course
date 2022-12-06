from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
  #Открыть сайт в браузере
  link = "http://suninjuly.github.io/file_input.html"
  browser = webdriver.Chrome()
  browser.get(link)

  #Заполнение текстовых полей
  firstname = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
  firstname.send_keys('Ivan')
  lastname = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
  lastname.send_keys('Petrov')
  email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
  email.send_keys('Smolensk@mail.ru')

  #Выбор файла(файл лежит в той же папке что и скрипт)
  file = browser.find_element(By.CSS_SELECTOR, "[name='file']")
  current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого скрипта
  file_name = "text.txt" # имя файла, который будем загружать на сайт
  file_path = os.path.join(current_dir, file_name) # получаем путь к file_example.txt
  file.send_keys(file_path)

  #Нажимаем кнопку
  btn = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
  btn.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

#Возможно кому-то будет полезно) Что бы ручками не создавать файл, можно сделать это с помощью python.

# with open("test.txt", "w") as file:
#     content = file.write("automationbypython")  # create test.txt file
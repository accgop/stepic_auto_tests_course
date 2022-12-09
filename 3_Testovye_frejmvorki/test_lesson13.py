from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class test_link1(unittest.TestCase):
    def test_link1(self):
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

    def test_link2(self):
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
input1.send_keys("Ivan")
input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
input2.send_keys("Petrov")
input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
input3.send_keys("Smolensk@mail.tu")

# Отправляем заполненную форму
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
input1.send_keys("Ivan")
input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
input2.send_keys("Petrov")
input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
input3.send_keys("Smolensk@mail.tu")

# Отправляем заполненную форму
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text


if __name__ == "__main__":
    unittest.main()
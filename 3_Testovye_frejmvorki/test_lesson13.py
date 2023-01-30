from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

#создаем класс с функциями проверки текста по ссылке
class test_link(unittest.TestCase):
    def test_link1(self):
        self.assertEqual(link_t("http://suninjuly.github.io/registration1.html"), "Congratulations! You have successfully registered!")

    def test_link2(self):
        self.assertEqual(link_t("http://suninjuly.github.io/registration2.html"), "Congratulations! You have successfully registered!")

#создаем функцию, в которой проходят все манипуляции с сайтом
def link_t(link):
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

    # находим элемент, содержащий текст и возвращаем его
    return browser.find_element(By.TAG_NAME, "h1").text

if __name__ == "__main__":
    unittest.main()
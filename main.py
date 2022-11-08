from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# browser = webdriver.Chrome()
# link = "https://SunInJuly.github.io/execute_script.html"
# browser.get(link)
# button = browser.find_element(By.TAG_NAME, "button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()
# time.sleep(10)
try:
    # link = "http://suninjuly.github.io/cats.html"
    # browser = webdriver.Chrome()
    # browser.implicitly_wait(5)
    # browser.get(link)

    # x_element = browser.find_element(By.ID, "input_value")
    # x = x_element.text
    # y = calc(x)

    # browser.find_element(By.NAME, "firstname").send_keys("Firsst")
    # browser.find_element(By.NAME, "lastname").send_keys("Second")
    # browser.find_element(By.NAME, "email").send_keys("test@test.ru")


    # current_dir = os.path.abspath(os.path.dirname(__file__))
    # file_path = os.path.join(current_dir, 'test.txt')
    # browser.find_element(By.NAME, "file").send_keys(file_path)

    # answer = browser.find_element(By.ID, "answer")
    # answer.send_keys(y)
    #
    # checkbox = browser.find_element(By.ID, "robotCheckbox")
    # checkbox.click()
    #
    # btn = browser.find_element(By.ID, "robotsRule")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
    # btn.click()



    # Отправляем заполненную форму
    # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # button.click()
    # time.sleep(1)
    # # browser.switch_to.alert.accept()
    # # time.sleep(1)
    # browser.switch_to.window(browser.window_handles[1])
    # x = browser.find_element(By.ID, "input_value").text
    # y = calc(x)
    # browser.find_element(By.ID, "answer").send_keys(y)
    # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # button.click()

    # browser.find_element(By.ID, "button").click()
    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 5 секунд


    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    browser.find_element(By.ID, "book").click()

    time.sleep(1)
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    button = browser.find_element(By.ID, "solve")
    button.click()

    # message = browser.find_element(By.ID, "verify_message")
    #
    # assert "successful" in message.text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

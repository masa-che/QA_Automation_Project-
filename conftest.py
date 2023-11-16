from datetime import datetime
import os
import allure

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')                      # при помощи этой фикстуры, тест выполняется один раз для каждой функции
def driver():
    options = Options()
    options.add_argument("user-data-dir=C:\\profile")  # создание временного профиля в браузере
    driver = webdriver.Chrome(options=options)         # запуск браузера с профилем add block
    #driver.get("https://google.com")                   # первоначальная страница запуска профиля
    options.add_argument('--headless')
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    #attach = driver.get_screenshot_as_png()            # в отчёте Allure в tear down будет прикреплён скрин вып теста
    #allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    #finish_time = str(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    #print(f'Test Finish: {finish_time}')
    driver.quit()

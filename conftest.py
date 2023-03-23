import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")  # при помощи этой фикстуры и scope function веб драйвер будет открываться и закрываться для каждого файла с тестами
def driver():
    webdriver.Chrome(ChromeDriverManager().install())               # запуск браузера chrome "и его обновление"
    options = Options()
    options.add_argument("user-data-dir=C:\\profile")               # создание профиля в браузере
    driver = webdriver.Chrome(chrome_options=options)               # запуск браузера с профилем
    driver.get("https://google.com")                                # первоначальная страница работы браузера
    driver.maximize_window()                                        # открытие окна браузера на весь экран
    yield driver                                                    # работает тело теста
    driver.quit()                                                   # "teardown"



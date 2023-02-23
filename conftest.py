import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")  # при помощи этой фикстуры и scope function веб драйвер будет открываться и закрываться для каждого файла с тестами
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())      # запуск браузера chrome "setup"
    driver.maximize_window()                                        # открытие окна браузера на весь экран
    yield driver                                                    # работает тело теста
    driver.quit()                                                   # "teardown"



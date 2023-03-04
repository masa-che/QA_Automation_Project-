
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):                      # поиск одного видимого елемента
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):                     # поиск всех видимых елементов
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):                       # ждёт появления элемента в DOM дереве
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):                     # ждёт появления всех элементов в DOM дереве
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):                   # поиск одного невидимого елемента
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):                     # для проверок кликабельности елемента
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):                                       # скролл к выбранному елементу
        self.driver.execute_script("arguments[0].scrollIntoView();", element)  # скрипт джавовый

# DOM - Объектная Модель Документа (Document Object Model) – это программный интерфейс (API) для HTML и XML документов

    def action_double_click(self, element):                                 # двойное нажатие lbm
        action = ActionChains(self.driver)   # библиотека действий с кликами мышки скролом и перетаскивать элементы etc
        action.double_click(element)         # синтаксис, выбор двойного клика левой кнопки мыши
        action.perform()                     # синтаксис, выполнение действия

    def action_right_click(self, element):                                  # клик rbm
        action = ActionChains(self.driver)   # библиотека действий с кликами мышки скролом и перетаскивать элементы etc
        action.context_click(element)        # синтаксис, выбор клика правой кнопкой мыши
        action.perform()                     # синтаксис, выполнение действия

    def action_drag_and_drop_by_offset(self, element, x_coord, y_coord):    # перетягивание слайдера по координатам
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coord, y_coord)
        action.perform()

    def action_move_to_element(self, element):                              # перемещение курсора мышки на элемент
        action = ActionChains(self.driver)   # библиотека действий с мышкой (скролл, клик, наведение на элемент etc)
        action.move_to_element(element)      # синтаксис, наведение курсора на элемент
        action.perform()                     # синтаксис, выполнение действия

    def remove_footer(self):
        # удаление по тегу - футера страницы (перекрывает кнопку "Submit", по факту это баг)
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        # удаление по id - кнопки в футере страницы
        # self.driver.execute_script("document.getElementsById('close-fixedban').remove();")

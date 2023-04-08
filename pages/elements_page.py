import base64
import requests
import time
import os
import random

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from generator.generator import generated_person, generated_file
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonLocators, \
    WebTablePageLocators, ButtonsPageLocators, LinksPageLocators, UpLoadAndDownloadPageLocators, \
    DynamicPropertiesPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    # Метод send_keys() в Python используется для ввода текста в текстовый элемент(поле)
    def fill_all_fields(self):
        person_info = next(generated_person())  # итератор next берёт по одному значению для каждого поля TextBox
        full_name = person_info.full_name       # взятое значение итератором next определяем в переменную full_name и тд
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    # функция берёт текст (метод .text) из поля board после нажатия кнопки submit и возвращает return-ом для проверки
    # для читабельности разобьём split-ом данные DOM-дерева для получения вводимых данных в функции fill_all_fields
    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):                                             # в функции используются методы class BasePage
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()  # клик кнопки выбора всех елементов checkbox

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
#       for i in item_list:                                               # for проходит по каждому из эл-ов ITEM_LIST
#            print(i.text)                                                # проверка возврата (checkbox tree) елементов
#            self.go_to_element(i)                                        # 'фокусировка' на каждом эл. ITEMS_LIST
#            i.click()
        count = 17                                                        # счётчик итераций
        while count != 0:                                                 # пока счётчик не равен нулю то:
            item = item_list[random.randint(1, 15)]                       # берём случайный элемент из списка ITEM_LIST
            if count > 0:                                                 # если счётчик больше нуля
                self.go_to_element(item)                                  # находим этот случайный элемент
                item.click()                                              # и кликаем его
                # print(item.text)                                        # принтуем текст выбранного item (проверка)
                count -= 1                                                # count минус один
            else:                                                         # иначе, когда count будет не больше нуля
                break                                                     # выход из цикла

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)  # список отм элементов CHECKED_ITEMS
        data = []                                                              # [list] в который будут записаны данные
        for box in checked_list:                                               # все отмеченные элементы из checked_list
            title_item = box.find_element(By.XPATH, self.locators.TITLE_ITEM)  # отбираются по xpath TITLE_ITEM
            print(title_item.text)                                             # принтуем для сравнения
            data.append(title_item.text)                                       # add в data текст отмеченных checkboxes
        return str(data).replace(' ', '').replace('.doc', '').lower()          # return отформатированный [список] data

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)   # список элементов OUTPUT_RESULT
        data = []                                                              # [list] в который будут записаны данные
        for item in result_list:                                               # все отмеченные элементы из result_list
            # print(item.text)                                                 # принтуем для сравнения
            data.append(item.text)                                             # add в data текст output checkboxes
        return str(data).replace(' ', '').lower()                              # return отформатированный [список] data

# str(data1).replace(' ', '').replace('.doc', '').lower()                      # строки из debug файла expecto_patronum
# str(data2).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonLocators()

    def check_radio_button(self, choice_rb):
        dictionary_rb = {'Yes': self.locators.RADIO_BUTTON_YES,
                         'Impressive': self.locators.RADIO_BUTTON_IMPRESSIVE,
                         'No': self.locators.RADIO_BUTTON_NO}
        # в переменную radio, из словаря будет выбран choice_rb локатор по значению ключа (Yes, Impressive, No)
        radio = self.element_is_visible(dictionary_rb[choice_rb]).click()

    def get_output_result(self):
        # возвращает текст в поле вывода при нажатии на radio_button
        return self.element_is_present(self.locators.OUTPUT_RESULT_RB).text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    def add_new_person(self):                                                           # добавление нового пользователя
        count = 1
        while count != 0:
            person_info = next(generated_person())                                      # итератор next берёт по одному значению для каждого поля WebTable
            firstname = person_info.first_name
            lastname = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()                   # нажатие на кнопку ADD
            # поиск локатора и добавление в него значение переменной firstname (и т.д.) сгенерированной пакетом faker
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(firstname)
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(lastname)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT).click()                   # клик по кнопке Submit
            count -= 1                                                              # после итерации счётчик уменьшается на единицу
            # возвращаем список для сравнения с output функции check_new_added_person заменяя int на str
            return [firstname, lastname, str(age), email, str(salary), department]

    def check_new_added_person(self):                                               # def для проверки правильности добавления данных
        person_list = self.elements_are_present(self.locators.FULL_PERSON_LIST)
        data = []                                                                   # [list] в который будут записаны данные
        for item in person_list:
            data.append(item.text.splitlines())   # получаем отдельные списки отдельных строк таблицы WebTable([],[],[])
        return data

    def search_some_person(self, key_word):  # функция нахождения пользователя по key word (вводимого в поле поиска)
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)     # key_word вписываем в строку поиска по таблице на странице WebTable

    def check_search_person(self):     # функция нахождения строки в webtable по delete button
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)        # поиск кнопки Delete в таблице для
        row = delete_button.find_element(By.XPATH, self.locators.ROW_PARENT)        # поиска родительской строки
        # возвращаем текст из строки таблицы webtable - списком (для проверки поиска одного списка в другом)
        return row.text.splitlines()

    def update_person_info(self):      # функция обновления age у пользователя, и возврата значения age (для проверки)
        person_info = next(generated_person())  # next берёт значение для переменной age путём генерации случ. числа
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()            # клик по "карандашу"
        self.element_is_visible(self.locators.AGE_INPUT).clear()                # очистка поля age
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)         # замена данных в поле age
        self.element_is_visible(self.locators.SUBMIT).click()                   # click по  кнопке Submit
        return str(age)                                                         # возвращаем age для дальнейшей проверки

    def delete_person(self):           # функция удаления строки с данными пользователя из таблицы webtable
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def check_deleted_person(self):    # функция поиска локатора отсутствия строк и return текста "No rows found"
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    def select_up_to_some_rose(self):  # функция выбора количества строк в таблице WebTable
        count = [5, 10, 20, 25, 50, 100]  # счётчик количества строк
        data = []                         # буфер для возврата данных
        for i in count:
            row_drop_box = self.element_is_visible(self.locators.ROWS_DROP_BOX)     # поиск drop_box
            # используем go_to_element потому что нужен точный якорь локатора drop_box на странице
            self.go_to_element(row_drop_box)
            row_drop_box.click()          # кликаем на drop_box
            # динамически меняем локатор при помощи редактирования строк (f)
            self.element_is_visible((By.CSS_SELECTOR, f'option[value="{i}"]')).click()
            data.append(self.check_count_rows())
        return data

    def check_count_rows(self):           # проверка количества строк и возврат длины(len)строк в числовом эквиваленте
        list_rows = self.elements_are_present(self.locators.FULL_PERSON_LIST)
        return len(list_rows)


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def click_on_different_button(self, type_click):
        if type_click == 'double':  # условие "double" подставим как аргумент к методу в самом тесте
            # используя библиотеку ActionChains кликаем кнопку "Double click" по нахождению её локатора
            self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON))
            # возвращаем текст результата клика по "Double click" (исп. функцию check_clicked_on_the_button)
            return self.check_clicked_on_the_button(self.locators.RESULT_DOUBLE)
        if type_click == 'right':

            self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
            return self.check_clicked_on_the_button(self.locators.RESULT_RIGHT)
        if type_click == 'click':
            self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()
            return self.check_clicked_on_the_button(self.locators.RESULT_CLICK_ME)

    # внутрення функция метода click_on_different_button
    # проверка клика на кнопку (RESULT_DOUBLE, RESULT_RIGHT, RESULT_CLICK_ME)
    # возвращает необходимый нам - текст локаторов, для assert в тесте
    def check_clicked_on_the_button(self, element):
        return self.element_is_present(element).text


class LinksPage(BasePage):
    locators = LinksPageLocators()

    def check_new_tab_home_link(self):     # открытие по ссылке новой вкладки и return "локаторной" ссылки и current_url
        home_link = self.element_is_visible(self.locators.HOME_LINK)
        link_href = home_link.get_attribute('href')  # get_attribute возвращает значение указанного атрибута элемента
        request = requests.get(link_href)  # href указывает ссылку: либо URL, либо якорь (ссылки хранятся в href)
        if request.status_code == 200:
            home_link.click()              # если ссылка статус 200 кликаем по ней
            # через driver переключаемся (switch) на вторую вкладку (handle[1])
            self.driver.switch_to.window(self.driver.window_handles[1])
            # в url кладём current_url для того чтобы сравнить та ли ссылка открылась через href
            url = self.driver.current_url  # current_url действующий url на открытой вкладке (new_tab)
            return link_href, url
        else:
            return link_href, request.status_code   # возврат линки и статус кода (если request.status_code != 200)

    def check_bad_link(self, url):                  # url из самого теста с (bad-request)
        request = requests.get(url)
        if request.status_code == 200:              # условие в if не отработает (ссылка с другим статус кодом)
            self.element_is_present(self.locators.BAD_REQUEST).click()
        else:
            return request.status_code              # условие else выполнится и вернёт статус код поломанной ссылки

    def check_unauthorized_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_present(self.locators.UNAUTHORIZED).click()
        else:
            return request.status_code


class UpLoadAndDownloadPage(BasePage):
    locators = UpLoadAndDownloadPageLocators()

    def upload_file(self):                       # функция авто-загрузки файла (создание файла, написано в generator.py)
        file_name, path = generated_file()       # from generator.generator.py import generated_file() (не забыть)
        # указываем путь(path) к файлу в сам input
        self.element_is_present(self.locators.INPUT_UPLOAD_FILE).send_keys(path)
        os.remove(path)                          # модуль os, remove - удалит наш файл
        # достанем текст wed при загрузке файла
        text = self.element_is_present(self.locators.UPLOADED_FILE_RESULT).text
        return file_name.split('\\')[-1], text.split('\\')[-1]

    def download_file(self):                        # функция для авто-загрузки файла
        # get_attribute возвращает значение указанного атрибута элемента (т.е. линку на файл картинки,
        # в котором зашифровано само изображение)
        link = self.element_is_present(self.locators.DOWNLOAD_FILE).get_attribute('href')
        # print(link)
        link_b = base64.b64decode(link)             # расшифровка побитно линки с кодом изображения
        # путь к файлу r- "сырая строка" обход экранирования (чтобы не ругалось на бэкслеш) и f- для редактирования
        path_file = rf'c:\Users\Maxim\PycharmProjects\QA_Pet_Automation_Project\filetest{random.randint(0, 101)}.jpg'
        # конструкция 'with as' - работает как менеджер создания контекста f: (работа с файлом) w - запись в файл
        # b - открывается как двоичный файл, + - режим чтения и записи
        with open(path_file, 'wb+') as f:
            offset = link_b.find(b'\xff\xd8')       # b-бинарник'\xff\xd8'- начальная точка поиска битового кода файла
            f.write(link_b[offset:])                # write в файл path_file всю кодировку начиная с offset и до конца
            check_file = os.path.exists(path_file)  # проверка записи файла, путь - path_file
            f.close()                               # закрытие файла
        os.remove(path_file)
        return check_file


class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesPageLocators()

    def check_changed_color(self):                  # возвращает цвета кнопки, до и после timeout web
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        # метод value_of_css_property('color')  вернёт значение цвета (rgba)
        color_button_before = color_button.value_of_css_property('color')
        time.sleep(5)
        color_button_after = color_button.value_of_css_property('color')
        return color_button_before, color_button_after

    def check_appear_button(self):                  # проверка появления кнопки, после timeout web
        try:
            self.element_is_present(self.locators.VISIBLE_AFTER_5S_BUTTON)
        except TimeoutException:
            return False
        return True

    def check_enable_button(self):                  # проверка кнопки, после timeout
        try:
            self.element_is_clickable(self.locators.ENABLE_BUTTON)
        except TimeoutException:
            return False
        return True

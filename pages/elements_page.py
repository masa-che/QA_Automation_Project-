from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonLocators
from pages.base_page import BasePage
import random


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
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)  # список отм елементов CHECKED_ITEMS
        data = []                                                              # буфер в который будут записаны данные
        for box in checked_list:                                               # все отмеченные элементы из checked_list
            title_item = box.find_element("xpath", self.locators.TITLE_ITEM)   # отбираются по xpath TITLE_ITEM
            # print(title_item.text)                                           # принтуем для сравнения
            data.append(title_item.text)                                       # add в data текст отмеченных checkboxes
        return str(data).replace(' ', '').replace('.doc', '').lower()          # return отформатированный [список] data

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)   # список елементов OUTPUT_RESULT
        data = []                                                              # буфер в который будут записаны данные
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

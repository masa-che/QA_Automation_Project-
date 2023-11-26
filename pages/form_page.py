import os
import time
import allure
# import pyautogui

from generator.generator import generated_person, generated_file, generated_subject
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class FormPage(BasePage):
    locators = FormPageLocators()

    @allure.step('fill in all fields')
    def fill_form_fields(self):
        # итератор next берёт по одному значению используя генератор данных - "generated_person" для полей Form
        person = next(generated_person())
        # generated_file(): функция генератор создания файла, возвращает имя файла и путь к нему
        file_name, path = generated_file()
        subject = generated_subject()
        with allure.step('remove footer'):
            self.remove_footer()
        with allure.step('filing fields ("First Name", "Last Name", "Email")'):
            self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.first_name)
            self.element_is_visible(self.locators.LAST_NAME).send_keys(person.last_name)
            self.element_is_visible(self.locators.EMAIL).send_keys(person.email)
        with allure.step('gender choice'):
            self.element_is_visible(self.locators.GENDER).click()
        with allure.step('filing field to "Mobile" number'):
            self.element_is_visible(self.locators.MOBILE).send_keys(person.mobile)
        # на форме баг, при введения даты рождения , происходит сбой работы формы заполнения данных
        # self.element_is_visible(self.locators.DATE_OF_BIRTH).click()
        # time.sleep(2)
        # self.element_is_visible(self.locators.DATE_OF_BIRTH).send_keys(Keys.CONTROL + "a")
        # time.sleep(2)
        # self.element_is_visible(self.locators.DATE_OF_BIRTH).send_keys(Keys.BACKSPACE)
        # time.sleep(2)
        # self.element_is_visible(self.locators.DATE_OF_BIRTH).send_keys('10 Feb 2008')
        # time.sleep(2)
        # self.element_is_visible(self.locators.DATE_OF_BIRTH).send_keys(Keys.ENTER)
        with allure.step('filing field "Subject"'):
            self.element_is_visible(self.locators.SUBJECT).send_keys(subject)
            self.element_is_visible(self.locators.SUBJECT).send_keys(Keys.RETURN)
        with allure.step('choice "Hobbies"'):
            self.element_is_visible(self.locators.HOBBIES).click()
        with allure.step('add picture to the form'):
            self.element_is_present(self.locators.FILE_INPUT).send_keys(path)
            os.remove(file_name)
        time.sleep(3)
        with allure.step('filing fild "Current Address"'):
            self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)
        # находим в DOM SELECT_STATE, смотрим что он is present, потом шагаем к елементу на web (go_to_element)
        with allure.step('filing field "Select State"'):
            self.go_to_element(self.element_is_present(self.locators.SELECT_STATE))
            self.element_is_visible(self.locators.SELECT_STATE).click()
            self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        with allure.step('filing field "Select Сity"'):
            self.element_is_visible(self.locators.SELECT_CITY).click()
            self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        with allure.step('click to "Submit" button'):
            self.go_to_element(self.element_is_present(self.locators.SUBMIT))
            self.element_is_visible(self.locators.SUBMIT).click()
        return person

    # функция для проверки вводимых данных с теми которые будут отображаться в таблице модального окна
    def form_result(self):
        # result_list содержит в себе локатор на 10-ть элементов 2-го столбца модального окна(RESULT_TABLE)
        result_list = self.elements_are_visible(self.locators.RESULT_TABLE)
        # создаём список
        data = []
        for item in result_list:
            # бежим по всем элементам item списка - result_list
            self.go_to_element(item)
            # добавляем текст элемента в список data
            data.append(item.text)
        return data


import time
import allure

from pages.form_page import FormPage


@allure.suite('Forms')
class TestForm:
    @allure.feature('FormPage')
    class TestFormPage:
        @allure.title('Check form')
        def test_form(self, driver):
            form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
            form_page.open()
            p = form_page.fill_form_fields()
            result = form_page.form_result()
            # в assert сравним (Имя Фамилию Email) возвращаемые внутри кортежа "p" и списка "result"
            # Объединяем внутри списка first_name и last_name т.к. result[0] - содержит в себе Имя и Фамилию
            assert [p.first_name + ' ' + p.last_name, p.email] == [result[0], result[1]], "the form hasn't been filled"


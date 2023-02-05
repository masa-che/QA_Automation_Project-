import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
            assert full_name == output_name, "the full name doesn't match"
            assert email == output_email, "the email doesn't match"
            assert current_address == output_cur_addr, "the current address doesn't match"
            assert permanent_address == output_per_addr, "the permanent_address doesn't match"
            time.sleep(15)

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()              # нажимаем на кнопку открывающую весь список checkbox
            check_box_page.click_random_checkbox()       # рандомный выбор checkbox елементов
            a = check_box_page.get_checked_checkboxes()  # возврат отмеченных рандомно чекбоксов (для проверки)
            b = check_box_page.get_output_result()       # возврат списка отмеченных рандомно чекбоксов (для проверки)
            # print(a)
            # print(b)
            assert a == b, "checkboxes haven't been selected"
            time.sleep(5)

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.check_radio_button('Yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.check_radio_button('Impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.check_radio_button('No')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', "'Yes' haven't been selected"
            assert output_impressive == 'Impressive', "'Impressive' haven't been selected"
            assert output_no == 'No', "'No' haven't been selected"


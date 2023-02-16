import time
import random

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UpLoadAndDownloadPage, DynamicPropertiesPage


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

    class TestWebTable:
        def test_web_table_add_person(self, driver):           # тест добавления нового пользователя в таблицу webtable
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            print(new_person)
            print(table_result)
            assert new_person in table_result

# ['Гурий', 'Гордеева', '31', 'nonna_15@example.net', '122251', 'Старшина']
# ['Гурий', 'Гордеева', '31', 'nonna_15@example.net', '122251', 'Старшина']

        def test_web_table_search_person(self, driver):        # тест поиск пользователя по ключ слову
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            # функция add_new_person возвращает список из шести элементов (firstname,lastname, age, salary...и тд)
            some_item_person = web_table_page.add_new_person()[random.randint(0, 5)]  # берём случайный элемент списка
            web_table_page.search_some_person(some_item_person)                       # поиск в таблице по случ элементу
            table_result = web_table_page.check_search_person()
            print(some_item_person)
            print(table_result)
            assert some_item_person in table_result, "person wasn't found in the WebTable"

        def test_web_table_update_person_info(self, driver):    # тест обновления данных пользователя в webtable
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]  # взятие "фамилии"[1] в работу, у нового пользователя
            web_table_page.search_some_person(lastname)    # поиск нового пользователя, в таблице, по фамилии
            age = web_table_page.update_person_info()      # заходим в редакцию пользователя меняем возраст (return age)
            row = web_table_page.check_search_person()     # возврат списка данных строки из webtable с изменённым age
            print(age)
            print(row)
            assert age in row, "The person card hasn't been changed"

        def test_web_table_delete_person(self, driver):        # тест удаление пользователя из webtable
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]          # взятие "email"[3] в работу, у нового пользователя
            web_table_page.search_some_person(email)            # поиск нового пользователя, в таблице, по email
            web_table_page.delete_person()                      # удаление пользователя
            no_rows = web_table_page.check_deleted_person()     # проверка удаления (поиск ключевой фразы no_rows)
            assert no_rows == "No rows found", " The user personal data hasn't been deleted "

        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rose()
            assert count == [5, 10, 20, 25, 50, 100], "The drop_box of rows in the table hasn't work properly"

    class TestButtonsPage:
        def test_different_click_buttons(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_on_different_button('double')
            right = button_page.click_on_different_button('right')
            click = button_page.click_on_different_button('click')
            assert double == "You have done a double click", "The double click button wasn't pressed"
            assert right == "You have done a right click", "The right click button wasn't pressed"
            assert click == "You have done a dynamic click", "The dynamic click button wasn't pressed"

    class TestLinksPage:

        def test_working_link(self, driver):                    # тест рабочей линки и открытие новой вкладки
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_home_link()
            print(href_link, current_url)
            assert href_link == current_url, "the link is broken or url is incorrect"

        def test_broken_link(self, driver):                     # тест не рабочей линки с status_code 400
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_bad_link('https://demoqa.com/bad-request')
            assert response_code == 400, "some thing wrong"     # 400-"Неверный запрос"

        def test_unauthorized_link(self, driver):               # тест линки с status_code 401
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_unauthorized_link('https://demoqa.com/unauthorized')
            assert response_code == 401, "some thing wrong"     # 401-"Неавторизованный"
            print(response_code)

# 201 - Created (Созданный)
# 204 - No Content (Без контента)

# 301 - Moved Permanently (перемещённый навсегда)

# 402 - Payment Required (в данный момент не используется, может использовать в дальнейшем)
# 403 - Forbidden (Запрещённый)
# 404 - Not Found (страницы не существует)

# 500 - Internal Server Error (ошибка на стороне сервера)

    class TestUpLoadAndDownload:

        def test_upload_file(self, driver):                          # тест загрузки файла
            upload_download_page = UpLoadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            file_name, result = upload_download_page.upload_file()
            assert file_name == result, "the file hasn't been uploaded"

        def test_download_file(self, driver):                        # тест скачивания файла
            upload_download_page = UpLoadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            check = upload_download_page.download_file()             # download возвращает path к файлу
            assert check is True, "the file hasn't been downloaded"  # путь существует - True, нет, файл не был скачан

    class TestDynamicPropertiesPage:

        def test_dynamic_properties(self, driver):                   # тест динамических свойств кнопки
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            color_before, color_after = dynamic_properties_page.check_changed_color()
            assert color_before != color_after, "color hasn't been changed"

        def test_appear_button(self, driver):                        # тест "появление" кнопки
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            appear_button = dynamic_properties_page.check_appear_button()
            assert appear_button is True, "button didn't appeared after 5 second"

        def test_enable_button(self, driver):                        # тест click кнопки(проверка кликабельности)
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            enable_button = dynamic_properties_page.check_enable_button()
            assert enable_button is True, "button didn't enabled after 5 second"




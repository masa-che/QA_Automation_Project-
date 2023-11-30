import allure

from pages.widgets_page import AccordionPage, AutoCompletePege, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage, SelectMenuPage
import time


@allure.suite('Widgets')
class TestWidgets:
    @allure.feature('Accordian Page')
    class TestAccordionPage:
        @allure.title('Check accordian widget')
        def test_accordian(self, driver):
            accordion_page = AccordionPage(driver, 'https://demoqa.com/accordian')
            accordion_page.open()
            first_title, first_content = accordion_page.check_accordion('first')
            second_title, second_content = accordion_page.check_accordion('second')
            third_title, third_content = accordion_page.check_accordion('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0, 'Incorrect title or missing text'
            assert second_title == 'Where does it come from?' and second_content > 0, 'Incorrect title or missing text'
            assert third_title == 'Why do we use it?' and third_content > 0, 'Incorrect title or missing text'

    @allure.feature('Autocomplete page')
    class TestAutoCompletePege:
        @allure.title('Check the autocomplete is filled')
        def test_fill_multi_autocomplete(self, driver):
            autocomplete_page = AutoCompletePege(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            colors = autocomplete_page.fill_input_multi()
            colors_result = autocomplete_page.check_color_in_multi()
            print(colors)
            print(colors_result)
            assert colors == colors_result, "the added colors are missing in the input"

        @allure.title('Check deletions from the multi autocomplete')
        def test_remove_value_multi_autocomplete(self, driver):
            autocomplete_page = AutoCompletePege(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.fill_input_multi()
            value_before, value_after = autocomplete_page.remove_input_value()
            print(value_before)
            print(value_after)
            assert value_before > value_after, "value was not deleted"

        @allure.title('Check deletions from the single autocomplete')
        def test_fill_single_autocomplete(self, driver):
            autocomplete_page = AutoCompletePege(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            color = autocomplete_page.fill_input_single()
            color_result = autocomplete_page.check_color_in_single()
            print(color)
            print(color_result)
            assert color == color_result, "the added color is missing in the input"

    @allure.feature('Date Picker Page')
    class TestDatePickerPage:
        @allure.title('Check change date')
        def test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date()
            print(value_date_before)
            print(value_date_after)
            assert value_date_before != value_date_after, "the date hasn't been changed"

        @allure.title('Check change date and time')
        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date_and_time()
            print(value_date_before)
            print(value_date_after)
            assert value_date_before != value_date_after, "the date or time have not been changed"

    @allure.feature('Slider Page')
    class TestSliderPage:
        @allure.title('Check moved slider')
        def test_slider(self, driver):
            slider = SliderPage(driver, 'https://demoqa.com/slider')
            slider.open()
            value_before, value_after = slider.change_slider_value()
            print(value_before)
            print(value_after)
            assert value_before != value_after, "the slider value hasn't been changed"

    @allure.feature('Progress Bar Page')
    class TestProgressBarPage:
        @allure.title('Check changed progress bar')
        def test_progress_bar(self, driver):
            progress_bar = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar.open()
            value_before, value_after = progress_bar.change_progress_bar_value()
            print(value_before)
            print(value_after)
            assert value_before != value_after, "the progress_bar value hasn't been changed"

    @allure.feature('Test Tabs Page')
    class TestTabsPage:
        @allure.title('Check switched tabs')
        def test_tabs(self, driver):
            tabs = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs.open()
            what_button, what_content = tabs.check_tabs('what')
            origin_button, origin_content = tabs.check_tabs('origin')
            use_button, use_content = tabs.check_tabs('use')
            more_button, more_content = tabs.check_tabs('more')
            assert what_button == 'What' and what_content > 0, "the tab 'What' wasn't clickable or the text is missing"
            assert origin_button == 'Origin' and origin_content > 0, "the tab 'Origin' wasn't clickable or the text is missing"
            assert use_button == 'Use' and use_content > 0, "the tab 'Use' wasn't clickable or the text is missing"
            assert more_button == 'More' and more_content > 0, "the tab 'More' wasn't clickable or the text is missing"

    @allure.feature('Tool Tips')
    class TestToolTips:
        @allure.title('Check tool tips ')
        def test_tool_tops(self, driver):
            tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tool_tips_page.open()
            button_text, field_text, contrary_text, section_text = tool_tips_page.check_tool_tips()
            assert button_text == 'You hovered over the Button', 'hover missing or incorrect content'
            assert field_text == 'You hovered over the text field', 'hover missing or incorrect content'
            assert contrary_text == 'You hovered over the Contrary', 'hover missing or incorrect content'
            assert section_text == 'You hovered over the 1.10.32', 'hover missing or incorrect content'

    @allure.feature('Menu Page')
    class TestMenu:
        @allure.title('Check all of the menu items')
        def test_menu_items(self, driver):
            menu_page = MenuPage(driver, 'https://demoqa.com/menu')
            menu_page.open()
            data = menu_page.check_menu()
            assert data == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1',
                            'Sub Sub Item 2', 'Main Item 3'], "menu items don't exist or have not been selected"

    @allure.feature('Select Menu')
    class TestSelectMenu:                                       # практическое задание вкладка "Widgets"-->"Select Menu"
        @allure.title('Filling and checking all elements for the "Select Menu" form')
        def test_select_menu_page(self, driver):
            select_menu_page = SelectMenuPage(driver, 'https://demoqa.com/select-menu')
            select_menu_page.open()
            select_value_before, select_value_after = select_menu_page.select_value()
            select_one_before, select_one_after = select_menu_page.select_one()
            color_before, color_after = select_menu_page.select_color_old_style()
            colors = select_menu_page.select_color_in_multiselect()
            colors_value = select_menu_page.check_color_in_multi()
            value_before, value_after = select_menu_page.remove_color_in_multiselect()
            car_before, car_after = select_menu_page.select_standard_multi()
            assert select_value_before != select_value_after, "the 'Select Value' field value hasn't been changed"
            assert select_one_before != select_one_after, "the 'Select One' field value hasn't been changed"
            assert color_before != color_after, "the 'Old Style Select Menu' value hasn't been changed"
            assert colors == colors_value, "the added colors are missing in the 'Multiselect drop down'"
            assert value_before > value_after, "value in 'Multiselect drop down' wasn't deleted"
            assert car_before != car_after, "value in 'Standard multi select' don't been selected"

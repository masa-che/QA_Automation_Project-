from pages.widgets_page import AccordionPage, AutoCompletePege, DatePickerPage, SliderPage, ProgressBarPage, TabsPage
import time


class TestWidgets:

    class TestAccordionPage:

        def test_accordian(self, driver):
            accordion_page = AccordionPage(driver, 'https://demoqa.com/accordian')
            accordion_page.open()
            first_title, first_content = accordion_page.check_accordion('first')
            second_title, second_content = accordion_page.check_accordion('second')
            third_title, third_content = accordion_page.check_accordion('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0, 'Incorrect title or missing text'
            assert second_title == 'Where does it come from?' and second_content > 0, 'Incorrect title or missing text'
            assert third_title == 'Why do we use it?' and third_content > 0, 'Incorrect title or missing text'

    class TestAutoCompletePege:

        def test_fill_multi_autocomplete(self, driver):
            autocomplete_page = AutoCompletePege(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            colors = autocomplete_page.fill_input_multi()
            colors_result = autocomplete_page.check_color_in_multi()
            print(colors)
            print(colors_result)
            assert colors == colors_result, "the added colors are missing in the input"

        def test_remove_value_multi_autocomplete(self, driver):
            autocomplete_page = AutoCompletePege(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.fill_input_multi()
            value_before, value_after = autocomplete_page.remove_input_value()
            print(value_before)
            print(value_after)
            assert value_before > value_after, "value was not deleted"

        def test_fill_single_autocomplete(self, driver):
            autocomplete_page = AutoCompletePege(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            color = autocomplete_page.fill_input_single()
            color_result = autocomplete_page.check_color_in_single()
            print(color)
            print(color_result)
            assert color == color_result, "the added color is missing in the input"

    class TestDatePickerPage:

        def test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date()
            print(value_date_before)
            print(value_date_after)
            assert value_date_before != value_date_after, "the date hasn't been changed"

        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date_and_time()
            print(value_date_before)
            print(value_date_after)
            assert value_date_before != value_date_after, "the date or time have not been changed"

    class TestSliderPage:

        def test_slider(self, driver):
            slider = SliderPage(driver, 'https://demoqa.com/slider')
            slider.open()
            value_before, value_after = slider.change_slider_value()
            print(value_before)
            print(value_after)
            assert value_before != value_after, "the slider value hasn't been changed"

    class TestProgressBarPage:

        def test_progress_bar(self, driver):
            progress_bar = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar.open()
            value_before, value_after = progress_bar.change_progress_bar_value()
            print(value_before)
            print(value_after)
            assert value_before != value_after, "the progress_bar value hasn't been changed"

    class TestTabsPage:

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


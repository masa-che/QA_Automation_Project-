from pages.widgets_page import AccordionPage, AutoCompletePege
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
            assert colors == colors_result, 'the added colors are missing in the input'

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
            assert color == color_result, 'the added color is missing in the input'


from locators.widgets_page_locators import AccordionPageLocators, AutoCompletePegeLocators, DatePickerPageLocators, \
    SliderPageLocators, ProgressBarPageLocators, TabsPageLocators, ToolTipsPageLocators, MenuPageLocators, \
    SelectMenuPageLocators
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from generator.generator import generated_color, generated_date, generated_select_value, generated_select_one, \
    generated_colors_old_select, generated_color_multiselect
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

import random
import time


class AccordionPage(BasePage):
    locators = AccordionPageLocators()

    # метод прохода по всем вкладкам accordion widget и возврат текста заголовков, длин текс-контента
    def check_accordion(self, accordion_num):
        accordion = {'first': {'title': self.locators.SECTION_FIRST,
                               'content': self.locators.SECTION_CONTENT_FIRST},
                     'second': {'title': self.locators.SECTION_SECOND,
                                'content': self.locators.SECTION_CONTENT_SECOND},
                     'third': {'title': self.locators.SECTION_THIRD,
                               'content': self.locators.SECTION_CONTENT_THIRD}
                     }

        section_title = self.element_is_visible(accordion[accordion_num]['title'])
        section_title.click()
        try:
            section_content = self.element_is_visible(accordion[accordion_num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordion[accordion_num]['content']).text
        return [section_title.text, len(section_content)]


class AutoCompletePege(BasePage):
    locators = AutoCompletePegeLocators()

    def fill_input_multi(self):             # добавление значений в поле MULTI_INPUT
        # sample - можно вытягивать СПИСКОМ несколько УНИКАЛЬНЫХ значений из списка color_name,
        # (k - количество значений взятых из списка)
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        # циклом фор бежим k раз внутри colors выбирая цвета для поля MULTI_INPUT
        for color in colors:
            input_multi = self.element_is_visible(self.locators.MULTI_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    def remove_input_value(self):           # удаление значения в поле MULTI_VALUE
        # определяем длину списка до удаления значений в поле локатора MULTI_VALUE
        count_value_before = len(self.elements_are_visible(self.locators.MULTI_VALUE))
        # в remove_button_list кладём все значения с кнопкой удаления элемента(MULTI_VALUE_REMOVE)
        # и циклом for пробегаем по всем этим элементам списка нажимая click() - происходит удаление элементов в поле
        remove_button_list = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
        # удаляем один элемент и выходим из цикла (в assert будем сравнивать длину списков before/after)
            break
        # определяем длину списка после удаления значений в поле локатора MULTI_VALUE
        count_value_after = len(self.elements_are_visible(self.locators.MULTI_VALUE))
        return count_value_before, count_value_after

    def check_color_in_multi(self):         # сравнение цветов из генератора, с цветами в поле MULTI_VALUE
        colors_list = self.elements_are_visible(self.locators.MULTI_VALUE)
        colors = []
        for color in colors_list:
            colors.append(color.text)
        return colors

    def fill_input_single(self):            # добавление значения в поле SINGLE_INPUT
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_visible(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        # Возвращаем из списка color элемент с нулевым индексом т.к. сравнивать будем с color.text (str)
        return color[0]

    def check_color_in_single(self):        # сравнение цвета из генератора, с цветом в поле MULTI_VALUE
        color = self.element_is_visible(self.locators.SINGLE_VALUE)
        return color.text


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    def select_date(self):                               # выбор даты
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        # забираем значение из поля для проверок в тесте (в DOM - value ="дата сегодняшнего дня")
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    def set_date_by_text(self, element, value):           # выбор по select, element-css элемент и value из generator
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def set_date_item_from_list(self, elements, value):   # выбор числа месяца(list)web, (if-первое вхождение и break)
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break

    def select_date_and_time(self):                       # выбор даты и времени (без select)
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_visible(self.locators.DATE_AND_TIME_MONTH).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, date.month)
        self.element_is_visible(self.locators.DATE_AND_TIME_YEAR).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_TIME_LIST, date.time)
        input_date_after = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_after = input_date_after.get_attribute('value')
        return value_date_before, value_date_after


class SliderPage(BasePage):
    locators = SliderPageLocators()

    def change_slider_value(self):                        # метод по работе с slide элементом
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.INPUT_SLIDER)
        # изменяем положение слайдера (библиотека action-chains, метод описан в BasePage)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(1, 100), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        # при помощи get_attribute, return-ом возвращаем значения 'value' на web селектора SLIDER_VALUE, до и после
        # манипуляций со слайдером
        return value_before, value_after


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    def change_progress_bar_value(self):                  # метод по работе с progress bar элементом
        value_before = self.element_is_present(self.locators.PROGRES_BAR_VALUE).text
        progress_bar_button = self.element_is_present(self.locators.PROGRESS_BAR_BUTTON)
        progress_bar_button.click()
        time.sleep(random.randint(2, 6))
        progress_bar_button.click()
        value_after = self.element_is_present(self.locators.PROGRES_BAR_VALUE).text
        return value_before, value_after


class TabsPage(BasePage):
    locators = TabsPageLocators()

    def check_tabs(self, tab_name):                       # метод по работе с вкладками (tabs)

        tabs = {'what':
                    {'title': self.locators.TABS_WHAT,
                     'content': self.locators.TABS_WHAT_CONTENT},
                'origin':
                    {'title': self.locators.TABS_ORIGIN,
                     'content': self.locators.TABS_ORIGIN_CONTENT},
                'use':
                    {'title': self.locators.TABS_USE,
                     'content': self.locators.TABS_USE_CONTENT},
                'more':
                    {'title': self.locators.TABS_MORE,
                     'content': self.locators.TABS_MORE_CONTENT}
                }

        button_name = self.element_is_visible(tabs[tab_name]['title'])
        button_name.click()
        text_content = self.element_is_visible(tabs[tab_name]['content']).text
        return button_name.text, len(text_content)


class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()

    # метод возврата текса из tool_tips
    def get_text_from_tool_tips(self, hover_elem, wait_elem):
        element = self.element_is_present(hover_elem)
        self.action_move_to_element(element)
        time.sleep(0.5)
        self.element_is_visible(wait_elem)
        tool_tip_text = self.element_is_visible(self.locators.TOOL_TIPS_INNERS)
        text = tool_tip_text.text
        return text

    def check_tool_tips(self):                              # метод проверки tool_tips на web (return текста tool_tips)
        tool_tip_text_button = self.get_text_from_tool_tips(self.locators.BUTTON, self.locators.TOOL_TIP_BUTTON)
        tool_tip_text_field = self.get_text_from_tool_tips(self.locators.FIELD, self.locators.TOOL_TIP_FIELD)
        tool_tip_text_cont = self.get_text_from_tool_tips(self.locators.CONTRARY_LINK, self.locators.TOOL_TIP_CONTRARY)
        tool_tip_text_sect = self.get_text_from_tool_tips(self.locators.SECTION_LINK, self.locators.TOOL_TIP_SECTION)
        return tool_tip_text_button, tool_tip_text_field, tool_tip_text_cont, tool_tip_text_sect


class MenuPage(BasePage):
    locators = MenuPageLocators()

    def check_menu(self):                                  # метод проверки заголовков в меню (1локатор для 8 элементов)
        menu_items_list = self.elements_are_present(self.locators.MENU_ITEM_LIST)
        data = []
        for item in menu_items_list:
            self.action_move_to_element(item)
            data.append(item.text)
        return data


# практическое задание вкладка "Widgets"-->"Select Menu"
class SelectMenuPage(BasePage):
    locators = SelectMenuPageLocators()

    def select_value(self):                                 # метод заполнения поля "Select Value"
        # генерация случайного значения из списка(list) указанных в bundle.js
        value = generated_select_value()
        # взятие текста изначально указанного в поле "Select Value" - необходимо для конечной проверки в тесте
        select_value_before = self.element_is_present(self.locators.SELECT_VALUE_BEFORE).text
        # изменение значения поля "Select Value", подставляем значение из нашего генератора
        self.element_is_visible(self.locators.SELECT_VALUE_INPUT).send_keys(value)
        # нажатие кнопки RETURN для закрытия drop_box "Select Value"
        self.element_is_visible(self.locators.SELECT_VALUE_INPUT).send_keys(Keys.RETURN)
        time.sleep(1)
        # взятие генерируемого текста поля "Select Value" генерируемого  - необходимо для конечной проверки в тесте
        select_value_after = self.element_is_present(self.locators.SELECT_VALUE_AFTER).text
        return select_value_before, select_value_after

    def select_one(self):                                   # метод заполнения поля "Select One"
        value = generated_select_one()
        select_one_before = self.element_is_present(self.locators.SELECT_ONE_BEFORE).text
        self.element_is_visible(self.locators.SELECT_ONE_INPUT).send_keys(value)
        self.element_is_visible(self.locators.SELECT_ONE_INPUT).send_keys(Keys.RETURN)
        time.sleep(1)
        select_one_after = self.element_is_present(self.locators.SELECT_VALUE_AFTER).text
        return select_one_before, select_one_after

    def select_color_old_style(self):                       # метод выбора цвета из "Old Style Select Menu"
        color = generated_colors_old_select()
        input_date = self.element_is_visible(self.locators.OLD_STYLE_SELECT)
        color_before = self.element_is_visible(self.locators.OLD_STYLE_SELECT).get_attribute('value')
        time.sleep(1)
        input_date.click()
        self.select_color_by_text(self.locators.OLD_STYLE_SELECT, color)
        time.sleep(1)
        input_date.click()
        time.sleep(1)
        color_after = self.element_is_visible(self.locators.OLD_STYLE_SELECT).get_attribute('value')
        return color_before, color_after

    def select_color_by_text(self, element, value):  # выбор по select, element-css элемент и value из generator
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def select_color_in_multiselect(self):           # метод добавления цветов в dropdown "Multiselect drop down"
        # sample - можно вытягивать СПИСКОМ несколько УНИКАЛЬНЫХ значений из списка color_name,
        # (k - количество значений взятых из списка)
        colors = random.sample(next(generated_color_multiselect()).color_name, k=random.randint(2, 4))
        # циклом фор бежим k раз внутри colors выбирая цвета для dropdown menu
        for color in colors:
            input_multi = self.element_is_visible(self.locators.MULTI_COLOR_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
            time.sleep(1)
        # colors - list
        return colors

    def check_color_in_multi(self):                  # метод для сравнения цветов из генератор,с цветами в "Multiselect drop down"
        colors_list = self.elements_are_visible(self.locators.MULTI_COLOR_VALUE)
        colors = []
        for color in colors_list:
            colors.append(color.text)
        # colors - list
        return colors

    def remove_color_in_multiselect(self):           # метод удаление значения в "Multiselect drop down"
        # определяем длину списка до удаления значений в поле локатора MULTI_COLOR_VALUE
        count_value_before = len(self.elements_are_visible(self.locators.MULTI_COLOR_VALUE))
        # в remove_button_list кладём все значения с кнопкой удаления элемента(MULTI_VALUE_COLOR_REMOVE)
        # и циклом for пробегаем по всем этим элементам списка нажимая click() - происходит удаление элементов в поле
        remove_button_list = self.elements_are_visible(self.locators.MULTI_COLOR_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            time.sleep(1)
        # удаляем один элемент и выходим из цикла (в assert будем сравнивать длину списков before/after)
            break
        # определяем длину списка после удаления значений в поле локатора MULTI_VALUE
        count_value_after = len(self.elements_are_visible(self.locators.MULTI_COLOR_VALUE))
        return count_value_before, count_value_after

    def select_standard_multi(self):                  # метод добавления авто в dropdown "Standard multi select"
        car_before = self.element_is_visible(self.locators.MULTI_STANDARD_SELECT).get_attribute('value')
        select_multi = Select(self.element_is_present(self.locators.MULTI_STANDARD_SELECT))
        select_multi.select_by_visible_text('Volvo')
        time.sleep(0.5)
        select_multi.select_by_visible_text('Saab')
        time.sleep(0.5)
        select_multi.select_by_visible_text('Audi')
        time.sleep(0.5)
        car_after = self.element_is_visible(self.locators.MULTI_STANDARD_SELECT).get_attribute('value')
        return car_before, car_after

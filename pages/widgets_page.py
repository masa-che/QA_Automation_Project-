from locators.widgets_page_locators import AccordionPageLocators, AutoCompletePegeLocators
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from generator.generator import generated_color
from selenium.common.exceptions import TimeoutException

import random
import time


class AccordionPage(BasePage):
    locators = AccordionPageLocators()

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









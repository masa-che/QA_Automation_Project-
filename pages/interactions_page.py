from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators
from pages.base_page import BasePage

import random
import time


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def get_sortable_items(self, elements):               # метод возврата текста всех значений tab "List"
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    def change_list_order(self):                          # метод для изменения порядка значений в tab "List"
        self.element_is_visible(self.locators.TAB_LIST).click()
        order_before = self.get_sortable_items(self.locators.LIST_ITEM)
        # меняем order_before случайным образом, изменяя положения двух строк в List (random.sample)
        item_list = random.sample(self.elements_are_visible(self.locators.LIST_ITEM), k=2)
        # для изменения местами элементов используем метод из base_page (action_drag_and_drop_to_element)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.LIST_ITEM)
        return order_before, order_after

    def change_grid_order(self):                          # метод для изменения порядка значений в tab "GRID"
        self.element_is_visible(self.locators.TAB_GRID).click()
        order_before = self.get_sortable_items(self.locators.GRID_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.GRID_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.GRID_ITEM)
        return order_before, order_after


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    # def click_selectable_item(self, elements):          # метод выбора одного случайного элемента и нажатие на него
    #     item_list = self.elements_are_visible(elements)
    #     random.sample(item_list, k=1)[0].click()

    def click_selectable_item(self, elements):            # метод выбора нескольких случайных элементов и нажатие на них
        item_list = random.sample(self.elements_are_visible(elements), k=random.randint(2, 4))
        for item in item_list:
            item.click()
            time.sleep(0.5)

    def select_list_item(self):                           # метод нажатия на елемент вкладки "List"
        self.element_is_visible(self.locators.TAB_LIST).click()
        self.click_selectable_item(self.locators.LIST_ITEM)
        time.sleep(2)
        active_element = self.element_is_visible(self.locators.LIST_ITEM_ACTIVE)
        return active_element.text

    def select_grid_item(self):                           # метод нажатия на елемент вкладки "Grid"
        self.element_is_visible(self.locators.TAB_GRID).click()
        self.click_selectable_item(self.locators.GRID_ITEM)
        active_element = self.element_is_visible(self.locators.GRID_ITEM_ACTIVE)
        return active_element.text




from locators.interactions_page_locators import SortablePageLocators
from pages.base_page import BasePage

import random


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def get_sortable_items(self, elements):                 # метод возврата текста всех значений tab "List"
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    def change_list_order(self):                            # метод для изменения порядка значений в tab "List"
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

    def change_grid_order(self):                            # метод для изменения порядка значений в tab "GRID"
        self.element_is_visible(self.locators.TAB_GRID).click()
        order_before = self.get_sortable_items(self.locators.GRID_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.GRID_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.GRID_ITEM)
        return order_before, order_after


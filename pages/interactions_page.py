from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators
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


class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    def get_px_from_width_height(self, value_of_size):    # метод для работы с шириной и высотой (pix пример 500, 300)
        # без split и replace получается громоздкий return --> width: 500px; height: 300px;........
        # первый split отсекает по ';' берём [0] элемент из списка 'width: 500px'
        # второй сплит отсекает по ':' берём [1] элемент из списка ' 500px'
        # replace убираем пробел, получаем '500px'
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    def get_max_min_size(self, element):
        size = self.element_is_present(element)
        size_value = size.get_attribute('style')
        return size_value

    def change_size_resizable_box(self):
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), 500, 200)
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), -700, -300)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        return max_size, min_size

    def change_size_resizable(self):
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE),
                                            random.randint(1, 500), random.randint(1, 300))
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE),
                                            random.randint(-200, -1), random.randint(-200, -1))
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        return max_size, min_size

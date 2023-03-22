from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators, DraggablePageLocators
from pages.base_page import BasePage

import random
import time
import re


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


class DroppablePage(BasePage):
    locators = DroppablePageLocators()

    def drop_simple(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_SIMPLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_SIMPLE)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        return drop_div.text

    def drop_accept(self):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        acceptable_div = self.element_is_visible(self.locators.ACCEPTABLE)
        not_acceptable_div = self.element_is_visible(self.locators.NOT_ACCEPTABLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_ACCEPT)
        self.action_drag_and_drop_to_element(not_acceptable_div, drop_div)
        text_not_acceptable = drop_div.text
        self.action_drag_and_drop_to_element(acceptable_div, drop_div)
        text_acceptable = drop_div.text
        return text_not_acceptable, text_acceptable

    def drop_prevent_propagation(self):
        self.element_is_visible(self.locators.PREVENT_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_PREVENT)
        greedy_inner_box = self.element_is_visible(self.locators.GREEDY_INNER_BOX)
        not_greedy_inner_box = self.element_is_visible(self.locators.NOT_GREEDY_INNER_BOX)
        self.action_drag_and_drop_to_element(drag_div, greedy_inner_box)
        text_greedy_inner_box = greedy_inner_box.text
        text_greedy_box = self.element_is_visible(self.locators.GREEDY_DROP_BOX_TEXT).text
        self.action_drag_and_drop_to_element(drag_div, not_greedy_inner_box)
        text_not_greedy_inner_box = not_greedy_inner_box.text
        text_not_greedy_box = self.element_is_visible(self.locators.NOT_GREEDY_DROP_BOX_TEXT).text
        return text_greedy_inner_box, text_greedy_box, text_not_greedy_inner_box, text_not_greedy_box

    def drop_revert_draggable(self, name_drag):
        drags = {
            'will':
                {'revert': self.locators.WILL_REVERT, },
            'not_will':
                {'revert': self.locators.NOT_REVERT},
        }
        self.element_is_visible(self.locators.REVERT_TAB).click()
        revert = self.element_is_visible(drags[name_drag]['revert'])
        drop_div = self.element_is_visible(self.locators.DROP_HERE_REVERT)
        self.action_drag_and_drop_to_element(revert, drop_div)
        position_after_move = revert.get_attribute('style')
        time.sleep(1)
        position_after_revert = revert.get_attribute('style')
        return position_after_move, position_after_revert


class DraggablePage(BasePage):
    locators = DraggablePageLocators()

    # определение позиции перетаскиваемого элемента(рандом)
    def get_before_and_after_position(self, drag_element):
        self.action_drag_and_drop_by_offset(drag_element, random.randint(-50, 250), random.randint(-50, 250))
        before_position = drag_element.get_attribute('style')
        self.action_drag_and_drop_by_offset(drag_element, random.randint(-50, 250), random.randint(-50, 250))
        after_position = drag_element.get_attribute('style')
        return before_position, after_position

    # заход на страницу/вкладку, поиск элемента, return координат нахождения элемента (до и после перетаскивания эл-та)
    def simple_drag_box(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME)
        before_position, after_position = self.get_before_and_after_position(drag_div)
        return before_position, after_position

    # re.findall(pattern, string) - Возвращает список всех найденных совпадений.
    # У метода findall() нет ограничений на поиск в начале или конце строки
    # забираем left координату нашего элемента(пример - 'position: relative; left: 372px; top: 0px;' - забираем 372)
    def get_left_position(self, position):
        left = re.findall(r'-\d+|\d+', position.split(";")[1])
        return left

    def get_top_position(self, position):
        top = re.findall(r'-\d+|\d+', position.split(";")[2])
        return top

    def constraint_axis_x(self):
        self.element_is_visible(self.locators.AXIS_TAB).click()
        only_x = self.element_is_visible(self.locators.ONLY_X)
        position_x = self.get_before_and_after_position(only_x)
        # print(position_x)
        # пример 'position: relative; left: 372px; top: 0px;'-это[0],'position: relative; left: 494px; top: 0px;'-это[1]
        left_x_before = self.get_left_position(position_x[0])
        left_x_after = self.get_left_position(position_x[1])
        top_x_before = self.get_top_position(position_x[0])
        top_x_after = self.get_top_position(position_x[1])
        # print(left_x_before)
        # print(top_x_before)
        # print(left_x_after)
        # print(top_x_after)
        return [left_x_before, top_x_before], [left_x_after, top_x_after]

    def constraint_axis_y(self):
        self.element_is_visible(self.locators.AXIS_TAB).click()
        only_y = self.element_is_visible(self.locators.ONLY_Y)
        position_y = self.get_before_and_after_position(only_y)
        # print(position_y)
        # пример 'position: relative; left: 0px; top: 278px;'-это[0],'position: relative; left: 0px; top: 467px;'-это[1]
        left_y_before = self.get_left_position(position_y[0])
        left_y_after = self.get_left_position(position_y[1])
        top_y_before = self.get_top_position(position_y[0])
        top_y_after = self.get_top_position(position_y[1])
        # print(left_y_before)
        # print(top_y_before)
        # print(left_y_after)
        # print(top_y_after)
        return [left_y_before, top_y_before], [left_y_after, top_y_after]

    def box_restricted_to_drag(self):
        self.element_is_visible(self.locators.CONTAINER_TAB).click()
        box_element = self.element_is_visible(self.locators.DRAGGABLE_BOX)
        drag_element = self.get_before_and_after_position(box_element)
        # print(drag_element)
        # пример position: relative; left: 195px; top: 41px;'это[0],'position: relative; left: 377px; top: 106px;'это[1]
        left_before = self.get_left_position(drag_element[0])
        left_after = self.get_left_position(drag_element[1])
        top_before = self.get_top_position(drag_element[0])
        top_after = self.get_top_position(drag_element[1])
        return float(left_before[0]), float(left_after[0]), float(top_before[0]), float(top_after[0])





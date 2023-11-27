import time

import allure

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DraggablePage


@allure.suite('Interactions')
class TestInteractions:
    @allure.feature('Sortable Page')
    class TestSortablePage:
        @allure.title('Check changed sortable list and grid')
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            print(list_before, list_after)
            print(grid_before, grid_after)
            assert list_before != list_after, "the order of the list hasn't been changed"
            assert grid_before != grid_after, "the order of the grid hasn't been changed"

    @allure.feature('Selectable Page')
    class TestSelectablePage:
        @allure.title('Check changed selectable list and grid')
        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            item_list = selectable_page.select_list_item()
            item_grid = selectable_page.select_grid_item()
            assert (len(item_list)) > 0, "no element were selected"
            assert (len(item_grid)) > 0, "no element were selected"

    @allure.feature('Resizable Page')
    class TestResizablePage:
        @allure.title('Check changed resizable boxes')
        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_box, min_box = resizable_page.change_size_resizable_box()
            max_resize, min_resize = resizable_page.change_size_resizable()
            print(max_box, min_box)
            print(max_resize, min_resize)
            assert ('500px', '300px') == max_box, "maximum size not equal to '500px', '300px'"
            assert ('150px', '150px') == min_box, "minimum size not equal to '150px', '150px'"
            assert min_resize != max_resize, "resizable hasn't been changed"

    @allure.feature('Droppable Page')
    class TestDroppablePage:
        @allure.title('Check simple droppable')
        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            drag_text = droppable_page.drop_simple()
            print(drag_text)
            assert drag_text == 'Dropped!', "the element hasn't been dropped"

        @allure.title('Check accept droppable')
        def test_accept_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text_not_accept, text_accept = droppable_page.drop_accept()
            print(text_not_accept)
            print(text_accept)
            assert text_not_accept != 'Dropped!', "the element has been accepted"
            assert text_accept == 'Dropped!', "the element hasn't been accepted"

        @allure.title('Check prevent propagation droppable')
        def test_prevent_propagation_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            greedy_inner, greedy, not_greedy_inner, not_greedy = droppable_page.drop_prevent_propagation()
            print(greedy_inner)
            print(greedy)
            print(not_greedy_inner)
            print(not_greedy)
            assert greedy_inner == 'Dropped!', "the elements texts hasn't been changed"
            assert greedy != 'Dropped!', "the elements texts has been changed"
            assert not_greedy_inner == 'Dropped!', "the elements texts hasn't been changed"
            assert not_greedy == 'Dropped!', "the elements texts hasn't been changed"

        @allure.title('Check revert draggable droppable')
        def test_revert_draggable_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            will_after_move, will_after_revert = droppable_page.drop_revert_draggable('will')
            not_will_after_move, not_will_after_revert = droppable_page.drop_revert_draggable('not_will')
            assert will_after_move != will_after_revert, 'the elements has not reverted'
            assert not_will_after_move == not_will_after_revert, 'the elements has  reverted'

    @allure.feature('Draggable Page')
    class TestDraggablePage:
        @allure.title('Check simple draggable')
        def test_simple_draggable(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            before_pos, after_pos = draggable_page.simple_drag_box()
            print(before_pos)
            print(after_pos)
            assert before_pos != after_pos, "element position hasn't been changed"

        @allure.title('Check axis restricted draggable')
        def test_axis_restricted_draggable(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            x_before, x_after = draggable_page.constraint_axis_x()
            y_before, y_after = draggable_page.constraint_axis_y()
            print(x_before)
            print(x_after)
            print(y_before)
            print(y_after)
            assert x_before[0][0] != x_after[0][0], "position hasn't changed"   # x - всегда меняется
            assert x_before[1][0] == x_before[1][0], "position hasn't changed"  # y - всегда ноль
            assert y_before[0][0] == y_after[0][0],  "position hasn't changed"  # x - всегда ноль
            assert y_before[1][0] != y_after[1][0],  "position hasn't changed"  # y - всегда меняется

        @allure.title('Check container restricted')
        def test_container_restricted(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            l_before, l_after, t_before, t_after = draggable_page.box_restricted_to_drag()
            print(l_before)
            print(l_after)
            print(t_before)
            print(t_after)
            assert -0.25 < l_before < 735.0 and -0.25 < l_after < 735.0, "box position hasn't crossed  restricted aria"
            assert -0.25 < t_before < 108.0 and -0.25 < t_after < 108.0, "box position hasn't crossed  restricted aria"
            time.sleep(3)



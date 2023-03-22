from selenium.webdriver.common.by import By


class SortablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    TAB_GRID = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    LIST_ITEM = (By.CSS_SELECTOR, 'div[id="demo-tabpane-list"] div[class="list-group-item list-group-item-action"]')
    GRID_ITEM = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"] div[class="list-group-item list-group-item-action"]')


class SelectablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    # не активный элемент "List"
    LIST_ITEM = (By.CSS_SELECTOR, 'ul[id="verticalListContainer"]'
                                  ' li[class="mt-2 list-group-item list-group-item-action"]')
    # активный с нажатием click, элемент
    LIST_ITEM_ACTIVE = (By.CSS_SELECTOR, 'ul[id="verticalListContainer"]'
                                         ' li[class="mt-2 list-group-item active list-group-item-action"]')
    TAB_GRID = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    # не активный элемент "Grid"
    GRID_ITEM = (By.CSS_SELECTOR, 'div[id="gridContainer"] li[class="list-group-item list-group-item-action"]')
    # активный с нажатием click, элемент
    GRID_ITEM_ACTIVE = (By.CSS_SELECTOR, 'div[id="gridContainer"]'
                                         ' li[class="list-group-item active list-group-item-action"]')


class ResizablePageLocators:
    # изменяемое окно в границах
    RESIZABLE_BOX = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"]')
    RESIZABLE_BOX_HANDLE = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"]'
                                             ' span[class="react-resizable-handle react-resizable-handle-se"]')

    # изменяемое окно без границ
    RESIZABLE = (By.CSS_SELECTOR, 'div[id="resizable"]')
    RESIZABLE_HANDLE = (By.CSS_SELECTOR, 'div[id="resizable"]'
                                         ' span[class="react-resizable-handle react-resizable-handle-se"]')


class DroppablePageLocators:
    # Simple
    SIMPLE_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-simple"]')
    DRAG_ME_SIMPLE = (By.CSS_SELECTOR, 'div[id="draggable"]')
    DROP_HERE_SIMPLE = (By.CSS_SELECTOR, '#simpleDropContainer #droppable')

    # Accept
    ACCEPT_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-accept"]')
    ACCEPTABLE = (By.CSS_SELECTOR, 'div[id="acceptable"]')
    NOT_ACCEPTABLE = (By.CSS_SELECTOR, 'div[id="notAcceptable"]')
    DROP_HERE_ACCEPT = (By.CSS_SELECTOR, '#acceptDropContainer #droppable')

    # Prevent Propagation
    PREVENT_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-preventPropogation"]')
    NOT_GREEDY_DROP_BOX_TEXT = (By.CSS_SELECTOR, 'div[id="notGreedyDropBox"] p:nth-child(1)')
    NOT_GREEDY_INNER_BOX = (By.CSS_SELECTOR, 'div[id="notGreedyInnerDropBox"]')
    GREEDY_DROP_BOX_TEXT = (By.CSS_SELECTOR, 'div[id="greedyDropBox"] p:nth-child(1)')
    GREEDY_INNER_BOX = (By.CSS_SELECTOR, 'div[id="greedyDropBoxInner"]')
    DRAG_ME_PREVENT = (By.CSS_SELECTOR, '#ppDropContainer #dragBox')

    # Revert Draggable
    REVERT_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-revertable"]')
    WILL_REVERT = (By.CSS_SELECTOR, 'div[id="revertable"]')
    NOT_REVERT = (By.CSS_SELECTOR, 'div[id="notRevertable"]')
    DROP_HERE_REVERT = (By.CSS_SELECTOR, '#revertableDropContainer #droppable')


class DraggablePageLocators:

    # Tab Simple
    SIMPLE_TAB = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-simple"]')
    DRAG_ME = (By.CSS_SELECTOR, 'div[id="draggableExample-tabpane-simple"] div[id="dragBox"]')

    # Tab Axis Restricted
    AXIS_TAB = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-axisRestriction"]')
    ONLY_X = (By.CSS_SELECTOR, 'div[id="restrictedX"]')
    ONLY_Y = (By.CSS_SELECTOR, 'div[id="restrictedY"]')

    # Tab Container Restricted
    CONTAINER_TAB = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-containerRestriction"]')
    DRAGGABLE_BOX = (By.CSS_SELECTOR, 'div[class ="draggable ui-widget-content ui-draggable ui-draggable-handle"]')
    WRAPPER_CONTAINER = (By.CSS_SELECTOR, 'div[id="containmentWrapper"]')



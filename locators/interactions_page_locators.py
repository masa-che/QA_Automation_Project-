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

from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    TAB_BUTTON = (By.CSS_SELECTOR, 'button[id="tabButton"]')            # кнопка "New Tab"
    NEW_TAB_TITLE = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')         # заголовок "This is a sample page"
    WINDOW_BUTTON = (By.CSS_SELECTOR, 'button[id="windowButton"]')      # кнопка "New Window"


from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    TAB_BUTTON = (By.CSS_SELECTOR, 'button[id="tabButton"]')            # кнопка "New Tab"
    NEW_TAB_TITLE = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')         # заголовок "This is a sample page"
    WINDOW_BUTTON = (By.CSS_SELECTOR, 'button[id="windowButton"]')      # кнопка "New Window"


class AlertsPageLocators:
    ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="alertButton"]')
    TIMER_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="timerAlertButton"]')
    CONFIRM_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="confirmButton"]')
    CONFIRM_RESULT = (By.CSS_SELECTOR, 'span[id="confirmResult"]')
    PROMPT_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="promtButton"]')
    PROMPT_RESULT = (By.CSS_SELECTOR, 'span[id="promptResult"]')


class FramesPageLocators:
    BIG_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    SMALL_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame2"]')
    FRAME_TITLE = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')           # локатор надписи внутри frames

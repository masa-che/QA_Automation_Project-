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


class NestedFramesPageLocators:
    PARENT_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    PARENT_TEXT = (By.CSS_SELECTOR, 'body')
    CHILD_FRAME = (By.CSS_SELECTOR, 'iframe[srcdoc="<p>Child Iframe</p>"]')
    CHILD_TEXT = (By.CSS_SELECTOR, 'p')


class ModalDialogsPageLocators:
    SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, 'button[id="showSmallModal"]')
    SMALL_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, 'button[id="closeSmallModal"]')
    SMALL_MODAL_BODY = (By.CSS_SELECTOR, 'div[class="modal-body"]')
    SMALL_MODAL_TITLE = (By.CSS_SELECTOR, 'div[id="example-modal-sizes-title-sm"]')

    LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, 'button[id="showLargeModal"]')
    LARGE_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, 'button[id="closeLargeModal"]')
    LARGE_MODAL_BODY = (By.CSS_SELECTOR, 'div[class="modal-body"] p')
    LARGE_MODAL_TITLE = (By.CSS_SELECTOR, 'div[id="example-modal-sizes-title-lg"]')


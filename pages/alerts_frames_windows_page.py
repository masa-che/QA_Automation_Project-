import time
import random

from pages.base_page import BasePage
from locators.alerts_frames_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators, FramesPageLocators, \
    NestedFramesPageLocators, ModalDialogsPageLocators


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_opened_new_tab(self):                             # метод открытия новой вкладки, с проверкой переключения
        self.element_is_visible(self.locators.TAB_BUTTON).click()
        # (switch_to.window - переключение браузера) - (windows_handles[1]- на вкладку[1] следующую после основной[0])
        self.driver.switch_to.window(self.driver.window_handles[1])
        # возврат текста локатора NEW_TAB_TITLE
        text_title = self.element_is_present(self.locators.NEW_TAB_TITLE).text
        return text_title

    def check_opened_new_window(self):                               # метод открытия окна, с проверкой переключения
        self.element_is_visible(self.locators.WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.NEW_TAB_TITLE).text
        return text_title


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def check_see_alert(self):                                       # метод переключения на alert окно
        self.element_is_visible(self.locators.ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_see_alert_after_5second(self):                         # метод переключения на alert окно (через 5секунд)
        self.element_is_visible(self.locators.TIMER_ALERT_BUTTON).click()
        time.sleep(5)
        # try:                                                       # если не проходит тест с time.sleep - uncomment
        #     alert_window = self.driver.switch_to.alert
        #     return alert_window.text
        # except UnexpectedAlertPresentException:
        #     alert_window = self.driver.switch_to.alert
        #     return alert_window.text
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_confirm_alert(self):                                   # метод переключения на alert и нажатия кнопки "Ок"
        self.element_is_visible(self.locators.CONFIRM_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()                                        # click "ok" in alert window
        # забираем текст локатора CONFIRM_RESULT
        text_result = self.element_is_present(self.locators.CONFIRM_RESULT).text
        return text_result

    def check_prompt_alert(self):                                    # метод переключения на alert - ввод текста - "Ok"
        text_in_field = f"Hello World{random.randint(0, 101)}"
        self.element_is_visible(self.locators.PROMPT_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text_in_field)
        alert_window.accept()                                        # click "ok" in alert window
        # забираем текст локатора PROMPT_RESULT
        text_result = self.element_is_present(self.locators.PROMPT_RESULT).text
        return text_in_field, text_result


class FramesPage(BasePage):
    locators = FramesPageLocators()

    def check_frames(self, frame_num):                                  # метод проверки frames (рамочек-остовов)
        if frame_num == "frame_big":                                    # "если" - 'frame_big' то
            frame = self.element_is_present(self.locators.BIG_FRAME)    # находим на web frame_big по селектору
            width = frame.get_attribute('width')                        # забираем ширину и высоту
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)                          # по локатору переключаемся на сам 'frame_big'
            text = self.element_is_present(self.locators.FRAME_TITLE).text  # забираем текст внутри frame
            self.driver.switch_to.default_content()                     # переключаемся на основную страницу web
            return [text, width, height]
        if frame_num == "frame_small":                                  # "если" - 'frame_small' то
            frame = self.element_is_present(self.locators.SMALL_FRAME)  # находим на web frame_small по селектору
            width = frame.get_attribute('width')                        # забираем ширину и высоту
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)                          # по локатору переключаемся на сам 'frame_small'
            text = self.element_is_present(self.locators.FRAME_TITLE).text  # забираем текст внутри frame
            self.driver.switch_to.default_content()                     # переключение на основную страницу web
            return [text, width, height]


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    def check_nested_frame(self):                                      # метод проверки вложенной рамки (frame)
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)                      # переключаемся на parent_frame
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text   # забираем текст внутри рамки
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)                       # переключаемся на child_frame
        child_text = self.element_is_present(self.locators.CHILD_TEXT).text     # забираем текст внутри рамки
        return parent_text, child_text


class ModalDialogsPage(BasePage):
    locators = ModalDialogsPageLocators()

    def check_small_modal_dialog(self):
        self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
        title_small = self.element_is_visible(self.locators.SMALL_MODAL_TITLE).text
        body_small = self.element_is_visible(self.locators.SMALL_MODAL_BODY).text
        self.element_is_visible(self.locators.SMALL_MODAL_CLOSE_BUTTON).click()
        return [title_small, len(body_small)]

    def check_large_modal_dialog(self):
        self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
        title_large = self.element_is_visible(self.locators.LARGE_MODAL_TITLE).text
        body_large = self.element_is_visible(self.locators.LARGE_MODAL_BODY).text
        self.element_is_visible(self.locators.LARGE_MODAL_CLOSE_BUTTON).click()
        return [title_large, len(body_large)]








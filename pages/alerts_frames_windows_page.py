import time
import random

from pages.base_page import BasePage
from locators.alerts_frames_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators


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

    def check_prompt_alert(self):                                   # метод переключения на alert - ввод текста - "Ok"
        text_in_field = f"Hello World{random.randint(0, 101)}"
        self.element_is_visible(self.locators.PROMPT_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text_in_field)
        alert_window.accept()                                       # click "ok" in alert window
        # забираем текст локатора PROMPT_RESULT
        text_result = self.element_is_present(self.locators.PROMPT_RESULT).text
        return text_in_field, text_result






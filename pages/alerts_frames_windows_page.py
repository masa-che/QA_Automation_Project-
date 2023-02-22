from pages.base_page import BasePage
from locators.alerts_frames_windows_locators import BrowserWindowsPageLocators


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_opened_new_tab(self):                             # метод открытия новой вкладки, с проверкой переключения
        self.element_is_visible(self.locators.TAB_BUTTON).click()
        # (switch_to.window - переключение браузера) - (windows_handles[1]- на вкладку[1] следующую после основной[0])
        self.driver.switch_to.window(self.driver.window_handles[1])
        # возврат текста локатора NEW_TAB_TITLE
        text_title = self.element_is_present(self.locators.NEW_TAB_TITLE).text
        return text_title

    def check_opened_new_window(self):                          # метод открытия окна, с проверкой переключения
        self.element_is_visible(self.locators.WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.NEW_TAB_TITLE).text
        return text_title








import time

import allure

from pages.alerts_frames_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, \
    ModalDialogsPage


@allure.suite('Alerts, Frame & Windows')
class TestAlertsFramesWindows:
    @allure.feature('Browser Windows')
    class TestBrowserWindows:
        @allure.title('Checking the opening of a new tab')
        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_tab_page.open()
            text_result = new_tab_page.check_opened_new_tab()
            assert text_result == "This is a sample page", "the new tab hasn't opened or an incorrect tab has opened"

        @allure.title('Checking the opening of a new window')
        def test_new_window(self, driver):
            new_window_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_window_page.open()
            text_result = new_window_page.check_opened_new_window()
            assert text_result == "This is a sample page", "the new window hasn't opened or an incorrect window has " \
                                                           "opened"

    @allure.feature('Alerts Page')
    class TestAlertsPage:
        @allure.title('Checking the opening of an alert')
        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == "You clicked a button", "Alert didn't show up "

        @allure.title('Checking the opening of the alert after 5 seconds')
        def test_see_alert_after_5second(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_see_alert_after_5second()
            assert alert_text == "This alert appeared after 5 seconds", "Alert didn't show up "

        @allure.title('Checking the opening of the alert with confirm')
        def test_confirm_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_confirm_alert()
            assert alert_text == "You selected Ok", "Alert didn't show up "

        @allure.title('Checking the opening of the alert with prompt')
        def test_prompt_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text, alert_text = alert_page.check_prompt_alert()
            assert text in alert_text, "Alert didn't show up "

    @allure.feature('Frame Page')
    class TestFramesPage:
        @allure.title('Check the page with frames')
        def test_frames(self, driver):
            frames_page = FramesPage(driver, 'https://demoqa.com/frames')
            frames_page.open()
            result_frame_big = frames_page.check_frames('frame_big')
            result_frame_small = frames_page.check_frames('frame_small')
            assert result_frame_big == ['This is a sample page', '500px', '350px'], "the frame doesn't exist"
            assert result_frame_small == ['This is a sample page', '100px', '100px'], "the frame doesn't exist"

    @allure.feature('Nested Page')
    class TestNestedFrames:
        @allure.title('Check the page with nested frames')
        def test_nested_frames(self, driver):
            nested_frames_page = NestedFramesPage(driver, 'https://demoqa.com/nestedframes')
            nested_frames_page.open()
            p_text, ch_text = nested_frames_page.check_nested_frame()
            assert p_text == 'Parent frame', "Nested frame doesn't exist"
            assert ch_text == 'Child Iframe', "Nested frame doesn't exist"

    @allure.feature('Modal Dialog Page')
    class TestModalDialogsPage:
        @allure.title('Check the page with modal dialogs')
        def test_modal_dialog(self, driver):
            modal_windows_page = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_windows_page.open()
            small = modal_windows_page.check_small_modal_dialog()
            large = modal_windows_page.check_large_modal_dialog()
            assert small[1] < large[1], "text from large dialog is less than text from small dialog"
            assert small[0] == 'Small Modal', "The header isn't 'Small modal'"
            assert large[0] == 'Large Modal', "The header isn't 'Large modal'"



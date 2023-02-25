import time
from pages.alerts_frames_windows_page import BrowserWindowsPage, AlertsPage, FramesPage


class TestAlertsFramesWindows:

    class TestBrowserWindows:
        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_tab_page.open()
            text_result = new_tab_page.check_opened_new_tab()
            assert text_result == "This is a sample page", "the new tab hasn't opened or an incorrect tab has opened"

        def test_new_window(self, driver):
            new_window_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_window_page.open()
            text_result = new_window_page.check_opened_new_window()
            assert text_result == "This is a sample page", "the new window hasn't opened or an incorrect window has " \
                                                           "opened"

    class TestAlertsPage:
        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == "You clicked a button", "Alert didn't show up "

        def test_see_alert_after_5second(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_see_alert_after_5second()
            assert alert_text == "This alert appeared after 5 seconds", "Alert didn't show up "

        def test_confirm_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_confirm_alert()
            assert alert_text == "You selected Ok", "Alert didn't show up "

        def test_prompt_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text, alert_text = alert_page.check_prompt_alert()
            assert text in alert_text, "Alert didn't show up "

    class TestFramesPage:
        def test_frames(self, driver):
            frames_page = FramesPage(driver, 'https://demoqa.com/frames')
            frames_page.open()
            result_frame_big = frames_page.check_frames('frame_big')
            result_frame_small = frames_page.check_frames('frame_small')
            assert result_frame_big == ['This is a sample page', '500px', '350px'], "the frame doesn't exist"
            assert result_frame_small == ['This is a sample page', '100px', '100px'], "the frame doesn't exist"

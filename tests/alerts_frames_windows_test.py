from pages.alerts_frames_windows_page import BrowserWindowsPage


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
            text_result = new_window_page.check_opened_new_tab()
            assert text_result == "This is a sample page", "the new window hasn't opened or an incorrect window has " \
                                                           "opened"


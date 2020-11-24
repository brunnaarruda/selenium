from selenium import webdriver


class BrowserUtils:
    def __init__(self):
        self.browser = None

    def open_page(self, browser='chrome', link=None):
        if browser == 'firefox':
            self.browser= webdriver.Firefox()
        elif browser == 'chrome':
            self.browser = webdriver.Chrome()
        self.browser.get(link)
        return self.browser

    def close_page(self, browser):
        # close one tab
        browser.close()

    def quit_page(self, browser):
        # close all tabs
        browser.quit()

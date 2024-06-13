import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class Browser():
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    chrome.implicitly_wait(5)
    chrome.set_page_load_timeout(10)

    def close(self):
        self.chrome.quit()
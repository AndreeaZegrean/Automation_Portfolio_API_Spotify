from seleniumbase import Driver

class Browser():

    def __init__(self):
        self.driver = Driver()
        self.driver.maximize_window()
        self.driver.get('https://open.spotify.com/')

    def closeBrowser(self):
        self.driver.quit()

from seleniumbase import Driver

class Browser():

    driver = Driver()
    driver.maximize_window()
    driver.get('https://open.spotify.com/')

    def closeBrowser(self):
        self.driver.quit()
import requests
from selenium.webdriver.common.by import By
from browser import Browser

class Generate_token(Browser):
    CLIENT_ID = "302fa0c6c00c481caa7099ebfabe3969"
    CLIENT_SECRET = "f3be51a3772b4d5f9c1dc36bcf195f7a"
    RESPONSE_TYPE= "code"
    ENCODED_REDIRECT_URI = "http%3A%2F%2Fitfactory.ro%2Fcallback"
    REDIRECT_URI = "https://oauth.pstmn.io/v1/browser-callback"
    SCOPE = "ugc-image-upload user-read-playback-state user-modify-playback-state user-read-currently-playing app-remote-control streaming playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify-public user-follow-modify user-follow-read user-read-playback-position user-top-read user-read-recently-played user-library-modify user-library-read user-read-email user-read-private"
    HOST = "https://accounts.spotify.com"
    USERNAME = (By.ID,"login-username")
    PASSSWORD = (By.ID,"login-password")
    LOG_IN_BUTTON =(By.ID,"login-button")
    AGREE_BUTTON = (By.CLASS_NAME,"jWBSO")
    GRANT_TYPE = "authorization_code"

    def create_authorize_endpoint(self):
        endpoint = self.HOST + "/authorize?client_id=" + self.CLIENT_ID+"&response_type="+self.RESPONSE_TYPE+"&redirect_uri="+self.ENCODED_REDIRECT_URI+"&scope="+self.SCOPE
        return endpoint

    def load_endpoint(self):
        self.driver.get(self.create_authorize_endpoint())

    def login_to_spotify(self):
        self.driver.find_element(*self.USERNAME).send_keys("deea2904@gmail.com")
        self.driver.find_element(*self.PASSSWORD).send_keys("Andreea29041988")
        self.driver.find_element(*self.LOG_IN_BUTTON).click()

    def authorize_login(self):
        self.driver.find_element(*self.AGREE_BUTTON).click()

    def get_code(self):
        url = self.driver.current_url
        code = url[url.index("=")+1:]
        return code

    def get_token(self):
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {
                "redirect_uri": self.REDIRECT_URI,
                "client_id": self.CLIENT_ID,
                "client_secret":self.CLIENT_SECRET,
                "code":self.get_code(),
                "grant_type":self.GRANT_TYPE
                }
        response = requests.post(self.HOST + "/api/token", data=data, headers=header)
        return response.json()["access_token"]

    def authorization(self):
        self.create_authorize_endpoint()
        self.load_endpoint()
        self.login_to_spotify()
        try:
            self.authorize_login()
        except:
            self.get_code()
        return f"Bearer {self.get_token()}"
import base.utils
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver


class DriverExtended(EventFiringWebDriver):
    
    def __init__(self, driver, event_listener, config):
        super().__init__(driver, event_listener)
        self.base_url = base.utils.HOST

    def load(self):
        self.get(self.base_url)

    def login(self):
        self.get(self.base_url + "/#/login")

    def users(self):
        self.get(self.base_url + "/#/users")

    def users_settings(self):
        self.get(self.base_url + "/#/settings")

    def recording(self):
        self.get(self.base_url + "/#/recording")

    def recording_settings(self):
        self.get(self.base_url + "/#/recording/settings")

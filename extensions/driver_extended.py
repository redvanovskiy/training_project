import base.utils
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver


class DriverExtended(EventFiringWebDriver):
    
    def __init__(self, driver, event_listener, config):
        super().__init__(driver, event_listener)
        self.base_url = base.utils.HOST

    def load(self):
        self.get(self.base_url)

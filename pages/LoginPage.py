import time

from base.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage(Base):
    _LOGIN_BUTTON = (By.CSS_SELECTOR, "#to_do")
    _LOGIN_INPUT = (By.CSS_SELECTOR, "#to_do")
    _PASSWORD_INPUT = (By.CSS_SELECTOR, "#to_do")


    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self.open()

    def set_username(self, username):
        self.send_keys(self._LOGIN_INPUT, username)

    def set_password(self, password):
        self.send_keys(self._PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click(self._LOGIN_BUTTON)

    def login(self, username, password):
        # TODO

import time

from base.base import Base
from selenium.webdriver.common.by import By


class LoginPage(Base):

    _LOGIN_INPUT = (By.NAME, "username")
    _PASSWORD_INPUT = (By.NAME, "password")
    _LOGIN_BUTTON = (By.CSS_SELECTOR, ".orangehrm-login-button")
    _REQUIRED1 = (By.CSS_SELECTOR, ".orangehrm-login-form :nth-child(2) > div > span")
    _REQUIRED2 = (By.CSS_SELECTOR, ".orangehrm-login-form :nth-child(3) > div > span")
    _INVALID_CRED_MSG = (By.CSS_SELECTOR, ".oxd-alert-content--error")
    _USER_PROFILE = (By.CSS_SELECTOR, ".oxd-userdropdown-name")
    _LOGOUT_BUTTON = (By.CSS_SELECTOR, ".oxd-userdropdown .oxd-dropdown-menu :nth-child(4)")

    def __init__(self, driver):
        super().__init__(driver)

    def set_username(self, username):
        self.send_keys(self._LOGIN_INPUT, username)

    def set_password(self, password):
        self.send_keys(self._PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click(self._LOGIN_BUTTON)

    def _login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_login_button()

    def check_required_login(self):
        self.visible(self._REQUIRED1)

    def check_required_password(self):
        self.visible(self._REQUIRED2)

    def check_invalid_credentials_message(self):
        self.visible(self._INVALID_CRED_MSG)

    def open_user_dropdown(self):
        self.click(self._USER_PROFILE)

    def click_logout_button(self):
        self.clickable(self._LOGOUT_BUTTON)
        self.click(self._LOGOUT_BUTTON)
        time.sleep(2)
        self.visible(self._LOGIN_BUTTON)

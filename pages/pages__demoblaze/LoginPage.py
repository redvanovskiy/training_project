import time

from base.base import Base
from selenium.webdriver.common.by import By


class LoginPage(Base):

    _LOGIN_BUTTON = (By.CSS_SELECTOR, "#login2")
    _LOGIN_INPUT = (By.CSS_SELECTOR, "#loginusername")
    _PASSWORD_INPUT = (By.CSS_SELECTOR, "#loginpassword")
    _SUBMIT_LOGIN_BUTTON = (By.CSS_SELECTOR, "#logInModal .btn.btn-primary")
    _LOGOUT_BUTTON = (By.CSS_SELECTOR, "#logout2")

    def __init__(self, driver):
        super().__init__(driver)

    def click_login_button(self):
        self.click(self._LOGIN_BUTTON)

    def set_username(self, username):
        self.send_keys(self._LOGIN_INPUT, username)

    def set_password(self, password):
        self.send_keys(self._PASSWORD_INPUT, password)

    def click_submit_login_button(self):
        self.click(self._SUBMIT_LOGIN_BUTTON)

    def _login(self, username, password):
        self.click_login_button()
        self.set_username(username)
        self.set_password(password)
        self.click_submit_login_button()

    def assert_text_in_alert(self, expected_text):
        time.sleep(2)
        alert = self.driver.switch_to.alert
        assert str(alert.text) == str(expected_text)

    def accept_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def click_logout_button(self):
        self.clickable(self._LOGOUT_BUTTON)
        self.click(self._LOGOUT_BUTTON)

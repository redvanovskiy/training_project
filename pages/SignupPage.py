import time

from base.base import Base
from selenium.webdriver.common.by import By


class SignupPage(Base):
    _SIGNUP_BUTTON = (By.CSS_SELECTOR, "#signin2")
    _SIGNUP_INPUT = (By.CSS_SELECTOR, "#sign-username")
    _PASSWORD_INPUT = (By.CSS_SELECTOR, "#sign-password")
    _SUBMIT_SIGNUP_BUTTON = (By.CSS_SELECTOR, "#signInModal > div > div > div.modal-footer > button.btn.btn-primary")


    def __init__(self, driver):
        super().__init__(driver)

    def click_signup_button(self):
        self.click(self._SIGNUP_BUTTON)

    def set_username(self, username):
        self.send_keys(self._SIGNUP_INPUT, username)

    def set_password(self, password):
        self.send_keys(self._PASSWORD_INPUT, password)

    def click_submit_login_button(self):
        self.click(self._SUBMIT_SIGNUP_BUTTON)

    def assert_text_in_alert(self, expected_text):
        time.sleep(2)
        alert = self.driver.switch_to.alert
        assert str(alert.text) == str(expected_text)

    def accept_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

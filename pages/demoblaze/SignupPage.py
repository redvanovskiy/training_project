import time

from base.base import Base
from selenium.webdriver.common.by import By


class SignupPage(Base):
    _SIGNUP_BUTTON = (By.CSS_SELECTOR, "#signin2")
    _SIGNUP_INPUT = (By.CSS_SELECTOR, "#sign-username")
    _PASSWORD_INPUT = (By.CSS_SELECTOR, "#sign-password")
    _SUBMIT_SIGNUP_BUTTON = (By.CSS_SELECTOR, "#signInModal .modal-footer .btn.btn-primary")

    def __init__(self, driver):
        super().__init__(driver)

    def click_signup_button(self):
        self.click(self._SIGNUP_BUTTON)

    def set_username(self, username):
        self.send_keys(self._SIGNUP_INPUT, username)

    def set_password(self, password):
        self.send_keys(self._PASSWORD_INPUT, password)

    def click_submit_signup_button(self):
        self.click(self._SUBMIT_SIGNUP_BUTTON)

    def _signup(self, username, password):
        self.click_signup_button()
        self.set_username(username)
        self.set_password(password)
        self.click_submit_signup_button()


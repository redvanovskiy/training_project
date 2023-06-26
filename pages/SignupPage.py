import time

from base.base import Base
from selenium.webdriver.common.by import By


class SignupPage(Base):
    _LOGIN_BUTTON = (By.CSS_SELECTOR, "#login2")
    _SIGNUP_BUTTON = (By.CSS_SELECTOR, "#signin2")
    _SIGNUP_INPUT = (By.CSS_SELECTOR, "#sign-username")
    _PASSWORD_INPUT = (By.CSS_SELECTOR, "#sign-password")
    _SUBMIT_SIGNUP_BUTTON = (By.CSS_SELECTOR, "#signInModal > div > div > div.modal-footer > button.btn.btn-primary")
    _LOGOUT_BUTTON = (By.CSS_SELECTOR, "#logout2")

    def __init__(self, driver):
        super().__init__(driver)

    def click_signup_button(self):
        self.click(self._SIGNUP_BUTTON)
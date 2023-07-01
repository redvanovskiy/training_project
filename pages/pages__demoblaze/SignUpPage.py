import time
import random
from random import randint
import string

from base.base import Base
from selenium.webdriver.common.by import By


class SignUpPage(Base):

    _SIGN_UP_BUTTON = (By.CSS_SELECTOR, "#signin2")
    _USERNAME_INPUT = (By.CSS_SELECTOR, "#sign-username")
    _PASSWORD_INPUT = (By.CSS_SELECTOR, "#sign-password")
    _SUBMIT_SIGN_UP_BUTTON = (By.CSS_SELECTOR, "#signInModal .btn.btn-primary")

    def __init__(self, driver):
        super().__init__(driver)

    def click_sign_up_button(self):
        self.click(self._SIGN_UP_BUTTON)

    def set_username(self, username):
        self.send_keys(self._USERNAME_INPUT, username)

    def set_password(self, password):
        self.send_keys(self._PASSWORD_INPUT, password)

    def random_string_generator(self, length, allowed_chars):
        return ''.join(random.choice(allowed_chars) for _ in range(length))

    def set_random_username(self, length):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))

    def set_random_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

    def click_submit_sign_up_button(self):
        self.click(self._SUBMIT_SIGN_UP_BUTTON)

    def _sign_up(self, username, password):
        self.click_sign_up_button()
        self.set_username(username)
        self.set_password(password)
        self.click_submit_sign_up_button()

    def _sign_up_with_random(self):
        random_username = self.set_random_username(8)
        random_password = self.set_random_password(12)
        self.click_sign_up_button()
        self.set_username(random_username)
        self.set_password(random_password)
        self.click_submit_sign_up_button()

    def assert_text_in_alert(self, expected_text):
        time.sleep(2)
        alert = self.driver.switch_to.alert
        assert str(alert.text) == str(expected_text)

    def accept_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()



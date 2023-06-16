import time

from base.base import Base
from selenium.webdriver.common.by import By


class ContactFormPage(Base):
    _CONTACT_BUTTON = (By.CSS_SELECTOR, "#exampleModal")
    _EMAIL_INPUT = (By.CSS_SELECTOR, "#recipient-email")
    _NAME_INPUT = (By.CSS_SELECTOR, "#recipient-name")
    _MESSAGE_INPUT = (By.CSS_SELECTOR, "#message-text")
    _CLOSE_BUTTON = (By.CSS_SELECTOR, "#exampleModal .btn.btn-secondary")
    _SEND_MESSAGE_BUTTON = (By.CSS_SELECTOR, "#exampleModal .btn.btn-primary")

    def __init__(self, driver):
        super().__init__(driver)

    def click_contact_button(self):
        self.click(self._CONTACT_BUTTON)

    def set_email(self, username):
        self.send_keys(self._EMAIL_INPUT, username)

    def set_username(self, username):
        self.send_keys(self._NAME_INPUT, username)

    def set_message(self, username):
        self.send_keys(self._MESSAGE_INPUT, username)

    def click_close_button(self):
        self.click(self._CLOSE_BUTTON)

    def click_send_message_button(self):
        self.click(self._SEND_MESSAGE_BUTTON)

    def sending_contact_form(self, email, username, message):
        self.click_contact_button()
        self.set_email(email)
        self.set_username(username)
        self.set_message(message)
        self.click_send_message_button()

    def assert_text_in_alert(self, expected_text):
        time.sleep(2)
        alert = self.driver.switch_to.alert
        assert str(alert.text) == str(expected_text)

    def accept_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()
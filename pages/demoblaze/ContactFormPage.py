from base.base import Base
from selenium.webdriver.common.by import By


class ContactFormPage(Base):
    _TITLE = (By.CSS_SELECTOR, "#exampleModalLabel")
    _CONTACT_EMAIL_INPUT = (By.CSS_SELECTOR, "#recipient-email")
    _CONTACT_NAME_INPUT = (By.CSS_SELECTOR, "#recipient-name")
    _MESSAGE_FIELD = (By.CSS_SELECTOR, "#message-text")
    _SEND_MESSAGE_BUTTON = (By.CSS_SELECTOR, "#exampleModal .modal-footer .btn-primary")
    _CLOSE_BUTTON = (By.CSS_SELECTOR, "#exampleModal .modal-footer .btn-secondary")
    _CLOSE_ICON = (By.CSS_SELECTOR, "#exampleModal .modal-header .close")

    def __init__(self, driver):
        super().__init__(driver)

    def assert_title(self, expected_text):
        self.assert_text(self._TITLE, expected_text)

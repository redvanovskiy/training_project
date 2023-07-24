import time
import random
from random import randint
import string

from base.base import Base
from selenium.webdriver.common.by import By


class ReportsListFieldsConstructorPage(Base):

    _LOGIN_INPUT = (By.CSS_SELECTOR, "#principal")
    _PASSWORD_INPUT = (By.CSS_SELECTOR, "#credential")
    _SIGN_IN_BUTTON = (By.CSS_SELECTOR, ".ant-row-middle .ant-btn-primary")

    _FIELDS_CONSTRUCTOR_BUTTON = (By.CSS_SELECTOR, ".ant-btn.const-btn")
    _CREATE_TEMPLATE_BUTTON = (By.CSS_SELECTOR, ".ant-row-end.action-panel .ant-btn-primary")
    _LIST = (By.CSS_SELECTOR, "section .ant-btn:nth-child(1)")
    _AGGREGATED = (By.CSS_SELECTOR, "section .ant-btn:nth-child(2)")
    _CONSOLIDATED = (By.CSS_SELECTOR, "section .ant-btn:nth-child(3)")
    _STATISTIC = (By.CSS_SELECTOR, "section .ant-btn:nth-child(4)")
    _CANCEL_BUTTON = (By.CSS_SELECTOR, ".footer-report-types .ant-btn:nth-child(1)")
    _CREATE_BUTTON = (By.CSS_SELECTOR, ".footer-report-types .ant-btn:nth-child(2)")
    _TEMPLATE_NAME = (By.CSS_SELECTOR, "main .ant-row .ant-input:nth-child(2)")

    def __init__(self, driver):
        super().__init__(driver)

    def set_username(self, username):
        self.send_keys(self._LOGIN_INPUT, username)

    def set_password(self, password):
        self.send_keys(self._PASSWORD_INPUT, password)

    def click_sign_in_button(self):
        self.click(self._SIGN_IN_BUTTON)

    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_sign_in_button()

    def open_fields_constructor(self):
        self.click(self._FIELDS_CONSTRUCTOR_BUTTON)

    def click_create_template_button(self):
        self.click(self._CREATE_TEMPLATE_BUTTON)

    def select_list(self):
        self.click(self._LIST)

    def select_aggregated(self):
        self.click(self._AGGREGATED)

    def select_consolidated(self):
        self.click(self._CONSOLIDATED)

    def select_statistic(self):
        self.click(self._STATISTIC)

    def click_cancel_button(self):
        self.click(self._CANCEL_BUTTON)

    def click_create_button(self):
        self.click(self._CREATE_BUTTON)

    def set_template_name(self, template_name):
        self.send_keys(self._TEMPLATE_NAME, template_name)

    def set_random_template_name(self, length):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))



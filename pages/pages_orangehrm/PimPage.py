import time
import random
import string

from base.base import Base
from selenium.webdriver.common.by import By


class PimPage(Base):
    _LOGIN_INPUT = (By.NAME, "username")
    _PASSWORD_INPUT = (By.NAME, "password")
    _LOGIN_BUTTON = (By.CSS_SELECTOR, ".orangehrm-login-button")
    _PIM_MODULE = (By.CSS_SELECTOR, ".oxd-sidepanel-body li:nth-child(2) > a")
    _EMPLOYEE_LIST = (By.CSS_SELECTOR, ".oxd-topbar-body-nav-tab.--visited > a")
    _ADD_BUTTON = (By.CSS_SELECTOR, ".orangehrm-paper-container .oxd-button")
    _FIRST_NAME_INPUT = (By.CSS_SELECTOR, ".orangehrm-firstname")
    _MIDDLE_NAME_INPUT = (By.CSS_SELECTOR, ".orangehrm-middlename")
    _LAST_NAME_INPUT = (By.CSS_SELECTOR, ".orangehrm-lastname")
    _REQUIRED1 = (By.CSS_SELECTOR, ".--name-grouped-field :nth-child(1) span")
    _REQUIRED2 = (By.CSS_SELECTOR, ".--name-grouped-field :nth-child(3) span")
    _SAVE_BUTTON = (By.CSS_SELECTOR, ".orangehrm-card-container .oxd-button--secondary")
    _PERSONAL_DETAILS = (By.CSS_SELECTOR, ".orangehrm-horizontal-padding.orangehrm-vertical-padding > h6")
    _SORT_BUTTON = (By.CSS_SELECTOR, ".bi-sort-alpha-up.oxd-icon-button__icon")
    _DECENDING = (By.CSS_SELECTOR, ".oxd-table-header :nth-child(2) > div > div > ul > li:nth-child(2) > span")
    _DELETE_BUTTON = (By.CSS_SELECTOR, ".oxd-table-body :nth-child(1) > div > :nth-child(9) button:nth-child(1)")
    _CONFIRM_BUTTON = (By.CSS_SELECTOR, ".oxd-button--label-danger")
    _SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#oxd-toaster_1")

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

    def open_pim_module(self):
        self.clickable(self._PIM_MODULE)
        self.click(self._PIM_MODULE)
        self.visible(self._EMPLOYEE_LIST)

    def click_add_button(self):
        self.click(self._ADD_BUTTON)

    def set_first_name(self, username):
        self.send_keys(self._FIRST_NAME_INPUT, username)

    def set_middle_name(self, username):
        self.send_keys(self._MIDDLE_NAME_INPUT, username)

    def set_last_name(self, username):
        self.send_keys(self._LAST_NAME_INPUT, username)

    def set_random_username(self, length):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))

    def click_save_button(self):
        self.click(self._SAVE_BUTTON)

    def _set_credentials(self):
        random_first_name = self.set_random_username(8)
        random_last_name = self.set_random_username(12)
        self.set_first_name(random_first_name)
        self.set_last_name(random_last_name)
        self.click_save_button()

    def check_new_profile(self):
        self.visible(self._PERSONAL_DETAILS)

    def sort_employee(self):
        self.click(self._SORT_BUTTON)
        time.sleep(1)
        self.click(self._DECENDING)

    def click_delete_button(self):
        self.click(self._DELETE_BUTTON)

    def click_confirm_button(self):
        self.click(self._CONFIRM_BUTTON)

    def check_success_message(self):
        self.visible(self._SUCCESS_MESSAGE)



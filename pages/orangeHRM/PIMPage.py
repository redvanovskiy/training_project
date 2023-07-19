from base.base import Base
from selenium.webdriver.common.by import By
import random
import string
import time


class PIMPage(Base):
    _ADD_BUTTON = (By.CSS_SELECTOR, ".oxd-button--secondary .bi-plus")
    _SEARCH_BUTTON = (By.CSS_SELECTOR, " .oxd-form-actions :nth-of-type(2)")
    _EMPLOYEE_NAME_SEARCH_FIELD = (By.CSS_SELECTOR, ".oxd-autocomplete-wrapper :nth-of-type(1) input")
    _FIRST_NAME_FIELD = (By.CSS_SELECTOR, "[name='firstName']")
    _MIDDLE_NAME_FIELD = (By.CSS_SELECTOR, "[name='middleName']")
    _LAST_NAME_FIELD = (By.CSS_SELECTOR, "[name='lastName']")
    _SAVE_BUTTON = (By.CSS_SELECTOR, "[type='submit'], .orangehrm-left-space")
    _EMPLOYEE_IMAGE = (By.CSS_SELECTOR, ".orangehrm-edit-employee-image-wrapper")
    _INFO_ALERT = (By.CSS_SELECTOR, "#oxd-toaster_1 .oxd-toast-start .oxd-toast-content.oxd-toast-content--info")
    _SUCCESS_ALERT = (By.CSS_SELECTOR, "#oxd-toaster_1 .oxd-toast-start .oxd-toast-content.oxd-toast-content--success")
    _DELETE_BUTTON = (By.CSS_SELECTOR, " .oxd-table-body :nth-child(9) button:nth-child(1)")
    _EDIT_BUTTON = (By.CSS_SELECTOR, " .oxd-table-body :nth-child(9) button:nth-child(2)")
    _ACCEPT_DELETE = (By.CSS_SELECTOR, ".oxd-button--label-danger.orangehrm-button-margin")
    _TITLE_RECORD_FOUND = (By.CSS_SELECTOR, " .orangehrm-paper-container >:nth-child(2) span")
    cred = ''.join(random.choice(string.hexdigits) for i in range(10))

    def __init__(self, driver):
        super().__init__(driver)

    def add_employee(self):
        self.click(self._ADD_BUTTON)
        time.sleep(1)
        self.send_keys(self._FIRST_NAME_FIELD, self.cred)
        self.send_keys(self._MIDDLE_NAME_FIELD, self.cred)
        self.send_keys(self._LAST_NAME_FIELD, self.cred)
        self.click(self._SAVE_BUTTON)

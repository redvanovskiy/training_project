from base.base import Base
from selenium.webdriver.common.by import By
import random
import string
import time


class AdminPage(Base):
    _ADD_BUTTON = (By.CSS_SELECTOR, ".oxd-button--secondary .bi-plus")
    _SEARCH_BUTTON = (By.CSS_SELECTOR, " .oxd-form-actions :nth-of-type(2)")
    _USERNAME_SEARCH_FIELD = (By.CSS_SELECTOR, ".oxd-form-row :nth-child(1) :nth-child(2) > input")
    _USER_ROLE_FIELD = (By.CSS_SELECTOR, ".oxd-layout-context form > :nth-child(1) > div > :nth-child(1) .oxd-select-text--after")
    _USER_ROLE_ADMIN = (By.CSS_SELECTOR, ".--positon-bottom :nth-child(2)")
    _EMPLOYEE_NAME = (By.CSS_SELECTOR, ".oxd-layout-context form > :nth-child(1) :nth-child(2) :nth-child(2) input")
    _EMPLOYEE_LISTBOX = (By.CSS_SELECTOR, "div.oxd-autocomplete-dropdown.--positon-bottom")
    _STATUS_FIELD = (By.CSS_SELECTOR, ".oxd-layout-context > div > div :nth-child(1) :nth-child(3) :nth-child(2) .oxd-select-text--after")
    _STATUS_ENABLED = (By.CSS_SELECTOR, ".--positon-bottom :nth-child(2)")
    _NAME_FIELD = (By.CSS_SELECTOR, " form :nth-child(1) :nth-child(4) :nth-child(2) input")
    _PASSWORD_FIELD = (By.CSS_SELECTOR, "form .user-password-cell :nth-child(2) input")
    _CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.oxd-form-row.user-password-row > div > div:nth-child(2) > div > div:nth-child(2) > input")
    _SAVE_BUTTON = (By.CSS_SELECTOR, "[type='submit'], .orangehrm-left-space")
    _LOADER = (By.CSS_SELECTOR, "div.oxd-form-loader")
    _username = ''.join(random.choice(string.hexdigits) for i in range(8))
    _password = ''.join(random.choice(string.hexdigits + string.punctuation) for i in range(10))

    def __init__(self, driver):
        super().__init__(driver)

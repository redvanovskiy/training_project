import time

from base.base import Base
from selenium.webdriver.common.by import By


class HomePage(Base):

    _LOGOUT_BUTTON = (By.CSS_SELECTOR, ".oxd-userdropdown .oxd-dropdown-menu :nth-child(4)")
    _LOGIN_BUTTON = (By.CSS_SELECTOR, ".orangehrm-login-button")

    def __init__(self, driver):
        super().__init__(driver)

    def click_logout_button(self):
        self.clickable(self._LOGOUT_BUTTON)
        self.click(self._LOGOUT_BUTTON)
        time.sleep(2)
        self.visible(self._LOGIN_BUTTON)

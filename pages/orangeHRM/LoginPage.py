from base.base import Base
from selenium.webdriver.common.by import By


class LoginPage(Base):
    _LOGIN_BUTTON = (By.CSS_SELECTOR, " .orangehrm-login-button")
    _FORGOT_PASSWORD_BUTTON = (By.CSS_SELECTOR, " .orangehrm-login-forgot-header")
    _LOGIN_INPUT = (By.CSS_SELECTOR, "[placeholder = 'Username']")
    _LOGIN_INPUT_ERROR = (By.CSS_SELECTOR, "[placeholder = 'Username'], .oxd-input .oxd-input--error")
    _REQUIRED_MESSAGE_LOGIN = (By.CSS_SELECTOR, "[placeholder = 'Username'], .oxd-text .oxd-input-group__message")
    _PASSWORD_INPUT = (By.CSS_SELECTOR, "[placeholder = 'Password']")
    _PASSWORD_INPUT_ERROR = (By.CSS_SELECTOR, "[placeholder = 'Password'], .oxd-input .oxd-input--error")
    _REQUIRED_MESSAGE_PASSWORD = (By.CSS_SELECTOR, "[placeholder = 'Password'], .oxd-text .oxd-input-group__message")
    _USER_MENU = (By.CSS_SELECTOR, ".oxd-userdropdown")
    _LOGOUT_BUTTON = (By.CSS_SELECTOR, ".oxd-dropdown-menu li:nth-of-type(4)")
    _FORGOT_PASSWORD_PAGE = (By.CSS_SELECTOR, ".orangehrm-forgot-password-card-note")
    _ALERT_TEXT = (By.CSS_SELECTOR, ".oxd-alert-content-text")

    def __init__(self, driver):
        super().__init__(driver)

    def click_login_button(self):
        self.click(self._LOGIN_BUTTON)

    def set_username(self, username):
        self.send_keys(self._LOGIN_INPUT, username)

    def set_password(self, password):
        self.send_keys(self._PASSWORD_INPUT, password)

    def click_forgot_button(self):
        self.click(self._FORGOT_PASSWORD_BUTTON)

    def _login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_login_button()

    def click_logout_button(self):
        self.clickable(self._USER_MENU)
        self.click(self._USER_MENU)
        self.clickable(self._LOGOUT_BUTTON)
        self.click(self._LOGOUT_BUTTON)
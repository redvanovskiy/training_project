from base.base import Base
from selenium.webdriver.common.by import By


class GroupListPage(Base):

    _LOGIN_INPUT = (By.CSS_SELECTOR, "#principal")
    _PASSWORD_INPUT = (By.CSS_SELECTOR, "#credential")
    _SIGN_IN_BUTTON = (By.CSS_SELECTOR, ".ant-row-middle .ant-btn-primary")

    _SEARCH_BUTTON = (By.CSS_SELECTOR, ".ant-col-lg-8 button:nth-child(1)")
    _SEARCH_FIELD = (By.CSS_SELECTOR, "._inp-wrap .ant-input")
    _CANCEL_SEARCH_BUTTON = (By.CSS_SELECTOR, ".ant-col-lg-8 ._inp-wrap :nth-child(3)")
    _FILTER_BUTTON = (By.CSS_SELECTOR, "#Path_1798")
    _UCCE_CHECKBOX = (By.CSS_SELECTOR, ".ant-popover-inner label:nth-child(1) input")
    _UCCX_CHECKBOX = (By.CSS_SELECTOR, ".ant-popover-inner label:nth-child(2) input")
    _GMSU_CHECKBOX = (By.CSS_SELECTOR, ".ant-popover-inner label:nth-child(3) input")
    _RESET_BUTTON = (By.CSS_SELECTOR, ".ant-popover-inner button:nth-child(1)")
    _OK_BUTTON = (By.CSS_SELECTOR, ".ant-popover-inner button:nth-child(2)")
    _COLLAPSE_BUTTON = (By.CSS_SELECTOR, ".search-elem .ant-btn:nth-of-type(2)")
    _EXPAND_BUTTON = (By.CSS_SELECTOR, ".ant-btn.to-small-view")

    def __init__(self, driver):
        super().__init__(driver)

    def set_username(self, username):
        self.send_keys(self._LOGIN_INPUT, username)

    def set_password(self, password):
        self.send_keys(self._PASSWORD_INPUT, password)

    def click_sign_in_button(self):
        self.click(self._SIGN_IN_BUTTON)

    def _login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_sign_in_button()

    def open_search_field(self):
        self.click(self._SEARCH_BUTTON)

    def set_search_key(self, key):
        self.send_keys(self._SEARCH_FIELD, key)

    def cansel_searching(self):
        self.click(self._CANCEL_SEARCH_BUTTON)

    def searching(self, key):
        self.open_search_field()
        self.set_search_key(key)
        self.cansel_searching()

    def open_filter(self):
        self.click(self._FILTER_BUTTON)

    def select_ucce_checkbox(self):
        self.click(self._UCCE_CHECKBOX)

    def select_uccx_checkbox(self):
        self.click(self._UCCX_CHECKBOX)

    def select_gmsu_checkbox(self):
        self.click(self._GMSU_CHECKBOX)

    def click_ok_button(self):
        self.click(self._OK_BUTTON)

    def cancel_previous_filter(self):
        self.open_filter()
        self.click(self._RESET_BUTTON)

    def click_collapse_button(self):
        self.click(self._COLLAPSE_BUTTON)

    def click_expand_button(self):
        self.click(self._EXPAND_BUTTON)

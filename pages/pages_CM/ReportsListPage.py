from base.base import Base
from selenium.webdriver.common.by import By


class ReportsListPage(Base):

    _LOGIN_INPUT = (By.CSS_SELECTOR, "#principal")
    _PASSWORD_INPUT = (By.CSS_SELECTOR, "#credential")
    _SIGN_IN_BUTTON = (By.CSS_SELECTOR, ".ant-row-middle .ant-btn-primary")

    _REPORTS_LIST_TAB = (By.CSS_SELECTOR, "#rc-tabs-4-tab-REPORTS")
    _FIRST_REPORT = (By.CSS_SELECTOR, ".list-container .report__item-parent")    #:nth_child(1)
    _GET_REPORT_BUTTON = (By.CSS_SELECTOR, ".footer-block .ant-btn-primary")
    _CANCEL_BUTTON = (By.CSS_SELECTOR, ".footer-block button:nth-child(1)")


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

    def open_reports_list_tab(self):
        self.click(self._REPORTS_LIST_TAB)

    def generate_first_reports(self):
        self.click(self._FIRST_REPORT)

    def click_get_report_button(self):
        self.click(self._GET_REPORT_BUTTON)

    def click_cancel_button(self):
        self.click(self._CANCEL_BUTTON)

    def download_first_report(self):
        self.click_get_report_button()
        self.click_get_report_button()



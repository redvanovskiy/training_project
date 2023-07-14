from base.base import Base
from selenium.webdriver.common.by import By


class RequestsListPage(Base):

    _LOGIN_INPUT = (By.CSS_SELECTOR, "#principal")
    _PASSWORD_INPUT = (By.CSS_SELECTOR, "#credential")
    _SIGN_IN_BUTTON = (By.CSS_SELECTOR, ".ant-row-middle .ant-btn-primary")

    _FIELDS_CONSTRUCTOR_BUTTON = (By.CSS_SELECTOR, ".ant-btn.const-btn")
    _REQUESTS_LIST_TAB = (By.CSS_SELECTOR, "#rc-tabs-4-tab-REQUESTS")
    _REFRESH_BUTTON = (By.CSS_SELECTOR, ".header button:nth-child(1)")
    _FILTER = (By.CSS_SELECTOR, ".header .filter-btn")
    _EXPORT_TO_EXCEL_BUTTON = (By.CSS_SELECTOR, ".header .ant-btn-primary")
    _SORT_BY_DIALLISTID = (By.CSS_SELECTOR, ".ant-table-header .ant-table-thead th:nth-child(2)")
    _SORT_BY_REQUESTID = (By.CSS_SELECTOR, ".ant-table-header .ant-table-thead th:nth-child(3)")
    _SORT_BY_REQUESTTEXT = (By.CSS_SELECTOR, ".ant-table-header .ant-table-thead th:nth-child(4)")
    _SORT_BY_CD_CALLRESULT = (By.CSS_SELECTOR, ".ant-table-header .ant-table-thead th:nth-child(5)")
    _SORT_BY_REQUESTDATETIME = (By.CSS_SELECTOR, ".ant-table-header .ant-table-thead th:nth-child(6)")
    _SORT_BY_CD_CALLSSTATUS = (By.CSS_SELECTOR, ".ant-table-header .ant-table-thead th:nth-child(7)")
    _SORT_BY_CD_CALLSMADE = (By.CSS_SELECTOR, ".ant-table-header .ant-table-thead th:nth-child(8)")
    _SORT_BY_SUCCESS = (By.CSS_SELECTOR, ".ant-table-header .ant-table-thead th:nth-child(9)")
    _SORT_BY_AGE = (By.CSS_SELECTOR, ".ant-table-header .ant-table-thead th:nth-child(10)")
    _DISPLAYED_COLUMNS = (By.CSS_SELECTOR, ".ant-table-header .ant-table-thead th:nth-child(11) span")
    _DISPLAYED_ALL_COLUMNS = (By.CSS_SELECTOR, ".ant-table-thead .ant-checkbox-input")
    _DISPLAYED_AGE = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-child(1) .ant-checkbox-input")
    _DISPLAYED_CD_CALLRESULT = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-child(2) .ant-checkbox-input")
    _DISPLAYED_CD_CALLSMADE = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-child(3) .ant-checkbox-input")
    _DISPLAYED_CD_CALLSSTATUS = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-child(4) .ant-checkbox-input")
    _DISPLAYED_DIALLISTID = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-child(5) .ant-checkbox-input")
    _DISPLAYED_REQUESTDATETIME = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-child(6) .ant-checkbox-input")
    _DISPLAYED_REQUESTID = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-child(7) .ant-checkbox-input")
    _DISPLAYED_REQUESTTEXT = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-child(8) .ant-checkbox-input")
    _DISPLAYED_SUCCESS = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-child(9) .ant-checkbox-input")
    _CANCEL_BUTTON = (By.CSS_SELECTOR, ".action-table-panel-wrapper button:nth-child(1)")
    _APPLY_BUTTON = (By.CSS_SELECTOR, ".action-table-panel-wrapper button:nth-child(2)")

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

    def open_requests_list_tab(self):
        self.click(self._REQUESTS_LIST_TAB)

    def click_refresh_button(self):
        self.click(self._REFRESH_BUTTON)

    def open_filter(self):
        self.click(self._FILTER)

    def click_export_to_excel_button(self):
        self.click(self._EXPORT_TO_EXCEL_BUTTON)

    def sort_by_diallistid(self):
        self.click(self._SORT_BY_DIALLISTID)

    def sort_by_requestid(self):
        self.click(self._SORT_BY_REQUESTID)

    def sort_by_requesttext(self):
        self.click(self._SORT_BY_REQUESTTEXT)

    def sort_by_cd_callresult(self):
        self.click(self._SORT_BY_CD_CALLRESULT)

    def sort_by_requestdatetime(self):
        self.click(self._SORT_BY_REQUESTDATETIME)

    def sort_by_cd_callstatus(self):
        self.click(self._SORT_BY_CD_CALLSSTATUS)

    def sort_by_cd_callmade(self):
        self.click(self._SORT_BY_CD_CALLSMADE)

    def sort_by_success(self):
        self.click(self._SORT_BY_SUCCESS)

    def sort_by_age(self):
        self.click(self._SORT_BY_AGE)

    def check_displayed_columns(self):
        self.click(self._DISPLAYED_COLUMNS)

    def select_all_columns(self):
        self.click(self._DISPLAYED_ALL_COLUMNS)

    def select_age_column(self):
        self.click(self._DISPLAYED_AGE)

    def select_cd_callresult_column(self):
        self.click(self._DISPLAYED_CD_CALLRESULT)

    def select_cd_callmade_column(self):
        self.click(self._DISPLAYED_CD_CALLSMADE)

    def select_cd_callstatus_column(self):
        self.click(self._DISPLAYED_CD_CALLSSTATUS)

    def select_diallistid_column(self):
        self.click(self._DISPLAYED_DIALLISTID)

    def select_requestdatetime_column(self):
        self.click(self._DISPLAYED_REQUESTDATETIME)

    def select_requestid_column(self):
        self.click(self._DISPLAYED_REQUESTID)

    def select_requesttext_column(self):
        self.click(self._DISPLAYED_REQUESTTEXT)

    def select_success_column(self):
        self.click(self._DISPLAYED_SUCCESS)

    def click_cansel_button(self):
        self.click(self._CANCEL_BUTTON)

    def click_apply_button(self):
        self.click(self._APPLY_BUTTON)
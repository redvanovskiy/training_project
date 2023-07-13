from base.base import Base
from selenium.webdriver.common.by import By


class ClientsListPage(Base):

    _LOGIN_INPUT = (By.CSS_SELECTOR, "#principal")
    _PASSWORD_INPUT = (By.CSS_SELECTOR, "#credential")
    _SIGN_IN_BUTTON = (By.CSS_SELECTOR, ".ant-row-middle .ant-btn-primary")

    _CLIENTS_LIST_TAB = (By.CSS_SELECTOR, "#rc-tabs-1-tab-CLIENTS")
    _REFRESH_BUTTON = (By.CSS_SELECTOR, ".header button:nth-child(1)")
    _FILTER = (By.CSS_SELECTOR, ".header .filter-btn")
    _EXPORT_TO_EXCEL_BUTTON = (By.CSS_SELECTOR, ".header .ant-btn-primary")
    _SORT_BY_PHONE = (By.CSS_SELECTOR, ".ant-table-header .ant-table-thead th:nth-child(2)")
    _SORT_BY_CIENTID = (By.CSS_SELECTOR, ".ant-table-header .ant-table-thead th:nth-child(3)")
    _SORT_BY_AGE = (By.CSS_SELECTOR, ".ant-table-header .ant-table-thead th:nth-child(4)")
    _SORT_BY_CIENTNAME = (By.CSS_SELECTOR, ".ant-table-header .ant-table-thead th:nth-child(5)")
    _DISPLAYED_COLUMNS = (By.CSS_SELECTOR, ".ant-table-header .ant-table-thead th:nth-child(6) span")
    _DISPLAYED_ALL_COLUMNS = (By.CSS_SELECTOR, ".ant-table-thead .ant-checkbox-input")
    _DISPLAYED_AGE = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-child(1) .ant-checkbox-input")
    _DISPLAYED_CLIENTID = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-child(2) .ant-checkbox-input")
    _DISPLAYED_CIENTNAME = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-child(3) .ant-checkbox-input")
    _DISPLAYED_PHONE = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-child(4) .ant-checkbox-input")
    _CANCEL_BUTTON = (By.CSS_SELECTOR, ".action-table-panel-wrapper button:nth-child(1)")
    _APPLY_BUTTON = (By.CSS_SELECTOR, ".action-table-panel-wrapper button:nth-child(2)")
    _CLIENT_DETAILS = (By.CSS_SELECTOR, ".ant-table-body tr:nth-child(2) .ant-table-cell svg")

    _ADD_FILTER_FIELD_BUTTON = (By.CSS_SELECTOR, ".cm_filter__button.add")
    _ADD_TO_PRESET_BUTTON = (By.CSS_SELECTOR, "#icon_add_to_favorite")
    _SELECT_FIELD = (By.CSS_SELECTOR, ".ant-select.filter-field__name")
    _SELECT_BATCHES = (By.CSS_SELECTOR, ".ant-select-show-search .ant-select-item.ant-select-item-option._bold-for-filter-option > div")


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

    def open_clients_list_tab(self):
        self.click(self._CLIENTS_LIST_TAB)

    def click_refresh_button(self):
        self.click(self._REFRESH_BUTTON)

    def open_filter(self):
        self.click(self._FILTER)

    def click_export_to_excel_button(self):
        self.click(self._EXPORT_TO_EXCEL_BUTTON)

    def sort_by_phone(self):
        self.click(self._SORT_BY_PHONE)

    def sort_by_clientid(self):
        self.click(self._SORT_BY_CIENTID)

    def sort_by_age(self):
        self.click(self._SORT_BY_AGE)

    def sort_by_clientname(self):
        self.click(self._SORT_BY_CIENTNAME)

    def check_displayed_columns(self):
        self.click(self._DISPLAYED_COLUMNS)

    def select_all_columns(self):
        self.click(self._DISPLAYED_ALL_COLUMNS)

    def select_age_column(self):
        self.click(self._DISPLAYED_AGE)

    def select_clientid_column(self):
        self.click(self._DISPLAYED_CLIENTID)

    def select_clientname_column(self):
        self.click(self._DISPLAYED_CIENTNAME)

    def select_phone_column(self):
        self.click(self._DISPLAYED_PHONE)

    def click_cansel_button(self):
        self.click(self._CANCEL_BUTTON)

    def click_apply_button(self):
        self.click(self._APPLY_BUTTON)


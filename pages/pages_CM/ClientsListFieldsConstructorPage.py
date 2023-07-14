from base.base import Base
from selenium.webdriver.common.by import By


class ClientsListFieldsConstructorPagePage(Base):

    _LOGIN_INPUT = (By.CSS_SELECTOR, "#principal")
    _PASSWORD_INPUT = (By.CSS_SELECTOR, "#credential")
    _SIGN_IN_BUTTON = (By.CSS_SELECTOR, ".ant-row-middle .ant-btn-primary")

    _FIELDS_CONSTRUCTOR_BUTTON = (By.CSS_SELECTOR, ".ant-btn.const-btn")
    _CLIENTS_LIST_TAB = (By.CSS_SELECTOR, "#rc-tabs-1-tab-CLIENTS")
    _ADD_FIELD_BUTTON = (By.CSS_SELECTOR, ".ant-row.ant-row-end.ant-row-space-between.action-panel .ant-btn-primary")
    _FIELD_NAME_INPUT = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(3) .ant-input")
    _FIELD_TITLE_INPUT = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(4) .ant-input")
    _DATA_TYPE_SELECTOR = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(5) .ant-select")

    _GROUP_CHECKBOX = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(6) .ant-checkbox-input")
    _INFO_ICON = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(6) .material-icons")
    _INPUT_TYPE_SELECTOR = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(7) .ant-select")

    _SHOW_TYPE_SELECTOR = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(8) .ant-select")
    _IS_UNIQUE_CHECKBOX = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(9) .ant-checkbox-input")
    _REQUIRED_CHECKBOX = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(10) .ant-checkbox-input")
    _HISTORY_CHECKBOX = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(11) .ant-checkbox-input")
    _FOR_FILTER_CHECKBOX = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(12) .ant-checkbox-input")
    _LENGTH = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(13) .ant-input")
    _DEFAULT_VALUE_INPUT = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(14) .ant-input")
    _ALL_SYMBOLS_CHECKBOX = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(15) .ant-checkbox-input")
    _DICTIONARY_SELECTOR = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(16) .ant-select")
    _RELATION_FIELD_SELECTOR = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(17) .ant-select")
    _SAVE_BUTTON = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(18) .save")
    _DELETE_LAST_FIELD_BUTTON = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(18) .toDeleteEditedElement")
    _CANCEL_DELETE_BUTTON = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(18) .ant-popover-content P:nth-child(2)")
    _CONFIRM_DELETE_BUTTON = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(18) .ant-popover-content P:nth-child(3)")
    _SUCCESS_MASSAGE = (By.CSS_SELECTOR, "body > div:nth-child(138) > div > span > div > div > div > div.ant-notification-notice-message")
    _CANCEL_ALL_BUTTON = (By.CSS_SELECTOR, ".setting-table-action-panel button:nth-child(1)")
    _SAVE_ALL_BUTTON = (By.CSS_SELECTOR, ".setting-table-action-panel button:nth-child(2)")
    _FIXED_ROW = (By.CSS_SELECTOR, ".ant-table-tbody .fixed")

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

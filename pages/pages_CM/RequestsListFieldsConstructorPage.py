import time
import random
from random import randint
import string

from base.base import Base
from selenium.webdriver.common.by import By


class RequestsListFieldsConstructorPage(Base):

    _LOGIN_INPUT = (By.CSS_SELECTOR, "#principal")
    _PASSWORD_INPUT = (By.CSS_SELECTOR, "#credential")
    _SIGN_IN_BUTTON = (By.CSS_SELECTOR, ".ant-row-middle .ant-btn-primary")

    _FIELDS_CONSTRUCTOR_BUTTON = (By.CSS_SELECTOR, ".ant-btn.const-btn")
    _REQUESTS_LIST_TAB = (By.CSS_SELECTOR, "#rc-tabs-4-tab-REQUESTS")
    _IMPORT_FIELDS_BUTTON = (By.CSS_SELECTOR, ".ant-row.ant-row-end.ant-row-space-between.action-panel button:nth-child(1)")
    _CLOSE_BUTTON = (By.CSS_SELECTOR, ".cm_filter__header .cm_filter__close")
    _ADD_FILTER_FIELD_BUTTON = (By.CSS_SELECTOR, ".cm_filter__main .cm_filter__button.add")
    _CANCEL_IMPORT_BUTTON = (By.CSS_SELECTOR, ".cm_filter__footer .cancel")
    _CONFIRM_IMPORT_BUTTON = (By.CSS_SELECTOR, ".cm_filter__footer .apply")
    _FIELDS_SELECTOR = (By.CSS_SELECTOR, ".filter-field .ant-select-selection-search")
    _FIRST_FIELD = (By.CSS_SELECTOR, ".ant-select-dropdown :nth-child(2) > div > div > div:nth-child(1)")
    _ADD_FIELD_BUTTON = (By.CSS_SELECTOR, ".ant-row.ant-row-end.ant-row-space-between.action-panel .ant-btn-primary")
    _FIELD_NAME_INPUT = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(3) .ant-input")
    _FIELD_TITLE_INPUT = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(4) .ant-input")
    _DATA_TYPE_SELECTOR = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(5) .ant-select")
    _STRING_TYPE = (By.CSS_SELECTOR, "tbody tr:nth-last-child(1) td:nth-child(5) .ant-select .ant-select-item:nth-child(1)")
    _DATETIME_TYPE = (By.CSS_SELECTOR, "tbody tr:nth-last-child(1) td:nth-child(5) .ant-select .ant-select-item:nth-child(2)")
    _DATE_TYPE = (By.CSS_SELECTOR, "tbody tr:nth-last-child(1) td:nth-child(5) .ant-select .ant-select-item:nth-child(3)")
    _TIME_TYPE = (By.CSS_SELECTOR, "tbody tr:nth-last-child(1) td:nth-child(5) .ant-select .ant-select-item:nth-child(4)")
    _INTEGER_TYPE = (By.CSS_SELECTOR, "tbody tr:nth-last-child(1) td:nth-child(5) .ant-select .ant-select-item:nth-child(5)")
    _FLOAT_TYPE = (By.CSS_SELECTOR, "tbody tr:nth-last-child(1) td:nth-child(5) .ant-select .ant-select-item:nth-child(6)")
    _TEXT_TYPE = (By.CSS_SELECTOR, "tbody tr:nth-last-child(1) td:nth-child(5) .ant-select .ant-select-item:nth-child(7)")
    _DICTIONARY_TYPE = (By.CSS_SELECTOR, "tbody tr:nth-last-child(1) td:nth-child(5) .ant-select .ant-select-item:nth-child(8)")
    _GROUP_CHECKBOX = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(6) .ant-checkbox-input")
    _INFO_ICON = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(6) .material-icons")
    _INPUT_TYPE_SELECTOR = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(7) .ant-select")
    _EDIT_TYPE = (By.CSS_SELECTOR, "tbody tr:nth-last-child(1) td:nth-child(7) .ant-select .ant-select-item:nth-child(1)")
    _PHONE_TYPE = (By.CSS_SELECTOR, "tbody tr:nth-last-child(1) td:nth-child(7) .ant-select .ant-select-item:nth-child(2)")
    _TEXT_TYPE_IF_STRING = (By.CSS_SELECTOR, "tbody tr:nth-last-child(1) td:nth-child(7) .ant-select .ant-select-item:nth-child(3)")
    _TEXT_TYPE_IF_INTEGER = (By.CSS_SELECTOR, "tbody tr:nth-last-child(1) td:nth-child(7) .ant-select .ant-select-item:nth-child(2)")
    _TEXT_TYPE_IF_TEXT = (By.CSS_SELECTOR, "tbody tr:nth-last-child(1) td:nth-child(7) .ant-select .ant-select-item:nth-child(1)")
    _COMBOBOX_TYPE = (By.CSS_SELECTOR, "tbody tr:nth-last-child(1) td:nth-child(7) .ant-select .ant-select-item:nth-child(1)")
    _RADIOBUTTONS_TYPE = (By.CSS_SELECTOR, "tbody tr:nth-last-child(1) td:nth-child(7) .ant-select .ant-select-item:nth-child(2)")
    _LIST_TYPE = (By.CSS_SELECTOR, "tbody tr:nth-last-child(1) td:nth-child(7) .ant-select .ant-select-item:nth-child(3)")
    _BUTTONS_TYPE = (By.CSS_SELECTOR, "tbody tr:nth-last-child(1) td:nth-child(7) .ant-select .ant-select-item:nth-child(4)")
    _SHOW_TYPE_SELECTOR = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(8) .ant-select")
    _MAIN_TYPE = (By.CSS_SELECTOR, "tbody tr:nth-last-child(1) td:nth-child(8) .ant-select .ant-select-item:nth-child(1)")
    _SECOND_TYPE = (By.CSS_SELECTOR, "tbody tr:nth-last-child(1) td:nth-child(8) .ant-select .ant-select-item:nth-child(2)")
    _IS_UNIQUE_CHECKBOX = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(9) .ant-checkbox-input")
    _REQUIRED_CHECKBOX = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(10) .ant-checkbox-input")
    _HISTORY_CHECKBOX = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(11) .ant-checkbox-input")
    _FOR_FILTER_CHECKBOX = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(12) .ant-checkbox-input")
    _LENGTH = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(13) .ant-input")
    _DEFAULT_VALUE_INPUT = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(14) .ant-input")
    _ALL_SYMBOLS_CHECKBOX = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(15) .ant-checkbox-input")
    _DICTIONARY_SELECTOR = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(16) .ant-select")
    _FIRST_DICTIONARY = (By.CSS_SELECTOR, "tbody tr:nth-last-child(1) td:nth-child(16) .ant-select .ant-select-item:nth-child(1)")
    _RELATION_FIELD_SELECTOR = (By.CSS_SELECTOR, ".ant-table-tbody tr:nth-last-child(1) td:nth-child(17) .ant-select")
    _FIRST_RELATION_FIELD = (By.CSS_SELECTOR, "tbody tr:nth-last-child(1) td:nth-child(17) .ant-select .ant-select-item:nth-child(1)")
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

    def click_add_field_button(self):
        self.click(self._ADD_FIELD_BUTTON)

    def set_field_name(self, field_name):
        self.send_keys(self._FIELD_NAME_INPUT, field_name)

    def set_field_title(self, field_title):
        self.send_keys(self._FIELD_TITLE_INPUT, field_title)

    def set_random_field_name(self, length):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))

    def set_random_field_title(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

    def open_data_type_selector(self):
        self.click(self._DATA_TYPE_SELECTOR)

    def select_string_type(self):
        self.click(self._STRING_TYPE)

    def select_datetime_type(self):
        self.click(self._DATETIME_TYPE)

    def select_date_type(self):
        self.click(self._DATE_TYPE)

    def select_time_type(self):
        self.click(self._TIME_TYPE)

    def select_integer_type(self):
        self.click(self._INTEGER_TYPE)

    def select_float_type(self):
        self.click(self._FLOAT_TYPE)

    def select_text_type(self):
        self.click(self._TEXT_TYPE)

    def select_dictionary_type(self):
        self.click(self._DICTIONARY_TYPE)

    def click_on_group_checkbox(self):
        self.click(self._GROUP_CHECKBOX)

    def open_input_type_selector(self):
        self.click(self._INPUT_TYPE_SELECTOR)

    def select_edit_type(self):
        self.click(self._EDIT_TYPE)

    def select_phone_type(self):
        self.click(self._PHONE_TYPE)

    def select_text_type_if_string(self):
        self.click(self._TEXT_TYPE_IF_STRING)

    def select_text_type_if_integer(self):
        self.click(self._TEXT_TYPE_IF_INTEGER)

    def select_text_type_if_text(self):
        self.click(self._TEXT_TYPE_IF_TEXT)

    def select_combobox_type(self):
        self.click(self._COMBOBOX_TYPE)

    def select_radiobuttons_type(self):
        self.click(self._RADIOBUTTONS_TYPE)

    def select_list_type(self):
        self.click(self._LIST_TYPE)

    def select_buttons_type(self):
        self.click(self._BUTTONS_TYPE)

    def open_show_type_selector(self):
        self.click(self._SHOW_TYPE_SELECTOR)

    def select_main_type(self):
        self.click(self._MAIN_TYPE)

    def select_second_type(self):
        self.click(self._SECOND_TYPE)

    def click_on_is_unique_checkbox(self):
        self.click(self._IS_UNIQUE_CHECKBOX)

    def click_on_required_checkbox(self):
        self.click(self._REQUIRED_CHECKBOX)

    def click_on_history_checkbox(self):
        self.click(self._HISTORY_CHECKBOX)

    def click_on_filter_checkbox(self):
        self.click(self._FOR_FILTER_CHECKBOX)

    def set_length(self, length):
        self.send_keys(self._LENGTH, length)

    def set_default_value(self, default_value):
        self.send_keys(self._DEFAULT_VALUE_INPUT, default_value)

    def click_on_all_symbols_checkbox(self):
        self.click(self._ALL_SYMBOLS_CHECKBOX)

    def open_dictionary_selector(self):
        self.click(self._DICTIONARY_SELECTOR)

    def select_first_dictionary(self):
        self.click(self._FIRST_DICTIONARY)

    def click_on_save_button(self):
        self.click(self._SAVE_BUTTON)

    def click_on_delete_last_field_button(self):
        self.click(self._DELETE_LAST_FIELD_BUTTON)

    def click_on_cancel_delete_button(self):
        self.click(self._CANCEL_DELETE_BUTTON)

    def click_on_confirm_delete_button(self):
        self.click(self._CONFIRM_DELETE_BUTTON)

    def click_on_cancel_all_button(self):
        self.click(self._CANCEL_ALL_BUTTON)

    def click_on_save_all_button(self):
        self.click(self._SAVE_ALL_BUTTON)

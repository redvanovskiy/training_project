import time
import random
from random import randint
import string

from base.base import Base
from selenium.webdriver.common.by import By


class GroupsListFieldsConstructorPage(Base):

    _LOGIN_INPUT = (By.CSS_SELECTOR, "#principal")
    _PASSWORD_INPUT = (By.CSS_SELECTOR, "#credential")
    _SIGN_IN_BUTTON = (By.CSS_SELECTOR, ".ant-row-middle .ant-btn-primary")

    _FIELDS_CONSTRUCTOR_BUTTON = (By.CSS_SELECTOR, ".ant-btn.const-btn")
    _ADD_BUTTON = (By.CSS_SELECTOR, ".ant-btn-primary.ant-btn-sm")
    _GROUP_NAME_INPUT = (By.CSS_SELECTOR, ".new-group header .ant-input")
    _COMMENT_INPUT = (By.CSS_SELECTOR, ".new-group main .ant-input")
    _SAVE_BUTTON = (By.CSS_SELECTOR, ".on-save-group .check")
    _SUCCESS_MASSAGE = (By.CSS_SELECTOR, ":nth-child(138) > div > span > div > div > div > div.ant-notification-notice-message")
    _ALERT_MASSAGE = (By.CSS_SELECTOR, ":nth-child(138) .notification-custom-error")
    _CLOSE_BUTTON = (By.CSS_SELECTOR, ".on-save-group :nth-child(2)")
    _USE_IN_CAMPAIGNS_BUTTON = (By.CSS_SELECTOR, ".ant-checkbox .ant-checkbox-input")
    _UCCE_RADIOBUTTON = (By.CSS_SELECTOR, ".ant-radio-group label:nth-child(1)")
    _UCCX_RADIOBUTTON = (By.CSS_SELECTOR, ".ant-radio-group label:nth-child(2)")
    _GMSU_CHECKBOX = (By.CSS_SELECTOR, ".gmsu-connector--wrapper .ant-checkbox-input")
    _LAST_ADDED_GROUP = (By.CSS_SELECTOR, "main > :nth-last-child(1) .cursor")
    _EDIT_BUTTON = (By.CSS_SELECTOR, "main :nth-last-child(1) button:nth-child(1)")
    _COPY_BUTTON = (By.CSS_SELECTOR, "main :nth-last-child(1) button:nth-child(2)")
    _EDIT_GROUP_NAME_INPUT = (By.CSS_SELECTOR, ".group-item-edited header .ant-input")
    _EDIT_COMMENT_INPUT = (By.CSS_SELECTOR, ".group-item-edited main .ant-input")
    _SAVE_CHANGES_BUTTON = (By.CSS_SELECTOR, ".group-item-edited__btns .check")
    _CLOSE_CHANGES_BUTTON = (By.CSS_SELECTOR, ".group-item-edited__btns :nth-child(2)")
    _USE_IN_CAMPAIGNS_EDIT_BUTTON = (By.CSS_SELECTOR, "main :nth-last-child(1) .ant-checkbox")
    _DELETE_BUTTON = (By.CSS_SELECTOR, "._delete-group > button")
    _CONFIRM_DELETE_BUTTON = (By.CSS_SELECTOR, ".ant-popover-inner-content button:nth-child(2)")
    _CANCEL_DELETE_BUTTON = (By.CSS_SELECTOR, ".ant-popover-inner-content button:nth-child(1)")

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

    def click_add_button(self):
        self.click(self._ADD_BUTTON)

    def set_group_name(self, name):
        self.send_keys(self._GROUP_NAME_INPUT, name)

    def set_comment(self, comment):
        self.send_keys(self._COMMENT_INPUT, comment)

    def set_random_group_name(self, length):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))

    def set_random_comment(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

    def click_save_button(self):
        self.click(self._SAVE_BUTTON)

    def close_alert(self):
        self.click(self._ALERT_MASSAGE)

    def click_close_button(self):
        self.click(self._CLOSE_BUTTON)

    def click_use_in_campaigns_button(self):
        self.click(self._USE_IN_CAMPAIGNS_BUTTON)

    def click_ucce_radiobutton(self):
        self.click(self._UCCE_RADIOBUTTON)

    def click_uccx_radiobutton(self):
        self.click(self._UCCX_RADIOBUTTON)

    def select_gmsu_checkbox(self):
        self.click(self._GMSU_CHECKBOX)

    def open_last_added_group(self):
        self.click(self._LAST_ADDED_GROUP)

    def click_edit_button(self):
        self.click(self._EDIT_BUTTON)

    def click_copy_button(self):
        self.click(self._COPY_BUTTON)

    def edit_group_name(self, name):
        self.send_keys(self._EDIT_GROUP_NAME_INPUT, name)

    def edit_comment(self, comment):
        self.send_keys(self._EDIT_COMMENT_INPUT, comment)

    def click_save_changes_button(self):
        self.click(self._SAVE_CHANGES_BUTTON)

    def click_close_changes_button(self):
        self.click(self._CLOSE_CHANGES_BUTTON)

    def click_use_in_campaigns_edit_button(self):
        self.click(self._USE_IN_CAMPAIGNS_EDIT_BUTTON)

    def click_delete_button(self):
        self.click(self._DELETE_BUTTON)

    def confirm_delete_button(self):
        self.click(self._CONFIRM_DELETE_BUTTON)

    def cancel_delete_button(self):
        self.click(self._CANCEL_DELETE_BUTTON)


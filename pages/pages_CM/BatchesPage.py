import time
import random
from random import randint
import string

from base.base import Base
from selenium.webdriver.common.by import By


class BatchesPage(Base):

    _LOGIN_INPUT = (By.CSS_SELECTOR, "#principal")
    _PASSWORD_INPUT = (By.CSS_SELECTOR, "#credential")
    _SIGN_IN_BUTTON = (By.CSS_SELECTOR, ".ant-row-middle .ant-btn-primary")

    _SWITCH_BUTTON = (By.CSS_SELECTOR, ".batches-header .ant-switch-handle")
    _CREATE_BATCH_BUTTON = (By.CSS_SELECTOR, ".batches-header .ant-btn")
    _BATCH_NAME = (By.CSS_SELECTOR, ".create-new .ant-row :nth-child(1) input")
    _BATCH_COMMENT = (By.CSS_SELECTOR, ".create-new .ant-row :nth-child(2) input")
    _CLOSE_BUTTON = (By.CSS_SELECTOR, ".create-new .material-icons")
    _CANCEL_BUTTON = (By.CSS_SELECTOR, ".create-new .action :nth-child(1)")
    _ADD_BUTTON = (By.CSS_SELECTOR, ".create-new .action :nth-child(2)")
    _SELECT_ALL_BATCHES_CHECKBOX = (By.CSS_SELECTOR, ".ant-row.list-batches-header .ant-checkbox-input")
    _BATCH_SORT_BUTTON = (By.CSS_SELECTOR, ".ant-row.list-batches-header :nth-child(3) .sort-flag__wrapper")
    _DATE_SORT_BUTTON = (By.CSS_SELECTOR, ".ant-row.list-batches-header :nth-child(5) .sort-flag__wrapper")
    _SELECT_FIRST_BATCH_CHECKBOX = (By.CSS_SELECTOR, ".list :nth-child(1) :nth-child(2) input")
    _SELECT_LAST_BATCH_CHECKBOX = (By.CSS_SELECTOR, ".list :nth-last-child(1) :nth-child(2) input")
    _HIDE_BATCHES_BUTTON = (By.CSS_SELECTOR, ".on-bottom-batch-container section button:nth-child(1)")
    _UNHIDE_BATCHES_BUTTON = (By.CSS_SELECTOR, ".on-bottom-batch-container section button:nth-child(2)")
    _DELETE_BATCHES_BUTTON = (By.CSS_SELECTOR, ".on-bottom-batch-container section button:nth-child(3)")
    _CONFIRM_DELETE_BUTTON = (By.CSS_SELECTOR, ".ant-popover-buttons button:nth-child(1)")
    _CANCEL_DELETE_BUTTON = (By.CSS_SELECTOR, ".ant-popover-buttons button:nth-child(2)")
    _ADD_ACTION_BUTTON = (By.CSS_SELECTOR, ".single:nth-last-child(1) .action :nth-child(1)")
    _EDIT_ACTION_BUTTON = (By.CSS_SELECTOR, ".single:nth-last-child(1) .action :nth-child(2)")
    _EDIT_BATCH_NAME_INPUT = (By.CSS_SELECTOR, ".edited-batch .ant-row :nth-child(1) .ant-input")
    _EDIT_BATCH_COMMENT_INPUT = (By.CSS_SELECTOR, ".edited-batch .ant-row :nth-child(1) .ant-input")
    _SAVE_CHANGES_BUTTON = (By.CSS_SELECTOR, ".edited-batch button:nth-child(2)")
    _CANCEL_CHANGES_BUTTON = (By.CSS_SELECTOR, ".edited-batch button:nth-child(1)")
    _REPLACE_DUPLICATES_CHECKBOX = (By.CSS_SELECTOR, ".subscribe-batch .ant-checkbox-input")
    _VIEW_MAPPING_FIELDS = (By.CSS_SELECTOR, ".subscribe-batch__btns .ant-btn:nth-child(2)")
    _CLOSE_MAPPING_FIELDS = (By.CSS_SELECTOR, ".subscribe-batch__mapped-fields-header--close span")
    _DOWNLOAD_EXCEL_BUTTON = (By.CSS_SELECTOR, ".subscribe-batch__btns .ant-btn:nth-child(3)")
    _UPLOAD_EXCEL_BUTTON = (By.CSS_SELECTOR, ".ant-upload.ant-upload-btn")
    _CANCEL_ADDING_BUTTON = (By.CSS_SELECTOR, "footer :nth-child(2) button:nth-child(1)")
    _ADD_CHANGES_BUTTON = (By.CSS_SELECTOR, "footer :nth-child(2) button:nth-child(2)")

    _SUCCESS_MASSAGE = (By.CSS_SELECTOR, "body > div:nth-child(138) > div > span > div > div > div > div.ant-notification-notice-message")
    _ALERT_MASSAGE = (By.CSS_SELECTOR, "body > div:nth-child(138) > div > span > div > div > div > div.ant-notification-notice-description")
    _CLOSE_MASSAGE = (By.CSS_SELECTOR, "body > div:nth-child(138) > div > span > div > a > span")
    # _HIDDEN_ROW = (By.CSS_SELECTOR, ".anticon-eye-invisible")

    def __init__(self, driver):
        super().__init__(driver)

    def set_username(self, username):
        self.send_keys(self._LOGIN_INPUT, username)

    def set_password(self, password):
        self.send_keys(self._PASSWORD_INPUT, password)

    def click_sign_in_button(self):
        self.click(self._SIGN_IN_BUTTON)

    def _login_(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_sign_in_button()

    def click_switch_button(self):
        self.click(self._SWITCH_BUTTON)

    def click_create_batch_button(self):
        self.click(self._CREATE_BATCH_BUTTON)

    def set_batch_name(self, batch_name):
        self.send_keys(self._BATCH_NAME, batch_name)

    def set_batch_comment(self, batch_comment):
        self.send_keys(self._BATCH_COMMENT, batch_comment)

    def set_random_batch_name(self, length):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))

    def set_random_batch_comment(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

    def click_close_button(self):
        self.click(self._CLOSE_BUTTON)

    def click_cancel_button(self):
        self.click(self._CANCEL_BUTTON)

    def click_add_button(self):
        self.click(self._ADD_BUTTON)

    def close_alert(self):
        self.click(self._ALERT_MASSAGE)

    def creating_new_batch(self,batch_name, batch_comment):
        self.set_batch_name(batch_name)
        self.set_batch_comment(batch_comment)
        self.click_add_button()

    def select_all_batches(self):
        self.click(self._SELECT_ALL_BATCHES_CHECKBOX)

    def click_batch_sort_button(self):
        self.click(self._BATCH_SORT_BUTTON)

    def click_date_sort_button(self):
        self.click(self._DATE_SORT_BUTTON)

    def select_first_batch(self):
        self.click(self._SELECT_FIRST_BATCH_CHECKBOX)

    def select_last_batch(self):
        self.click(self._SELECT_LAST_BATCH_CHECKBOX)

    def click_hide_batches_button(self):
        self.click(self._HIDE_BATCHES_BUTTON)

    def click_unhide_batches_button(self):
        self.click(self._UNHIDE_BATCHES_BUTTON)

    def click_delete_batches_button(self):
        self.click(self._DELETE_BATCHES_BUTTON)

    def click_confirm_delete(self):
        self.click(self._CONFIRM_DELETE_BUTTON)

    def click_cancel_delete(self):
        self.click(self._CANCEL_DELETE_BUTTON)

    def click_add_action_button(self):
        self.click(self._ADD_ACTION_BUTTON)

    def click_edit_action_button(self):
        self.click(self._EDIT_ACTION_BUTTON)

    def click_save_changes_button(self):
        self.click(self._SAVE_CHANGES_BUTTON)

    def edit_batch_name(self, name):
        self.send_keys(self._EDIT_BATCH_NAME_INPUT, name)

    def edit_batch_comment(self, comment):
        self.send_keys(self._EDIT_BATCH_COMMENT_INPUT, comment)

    def click_close_changes_button(self):
        self.click(self._CANCEL_CHANGES_BUTTON)

    def click_replace_duplicates_checkbox(self):
        self.click(self._REPLACE_DUPLICATES_CHECKBOX)

    def view_mapping_fields(self):
        self.click(self._VIEW_MAPPING_FIELDS)

    def close_mapping_fields(self):
        self.click(self._CLOSE_MAPPING_FIELDS)

    def click_download_excel_button(self):
        self.click(self._DOWNLOAD_EXCEL_BUTTON)

    def click_upload_excel_button(self):
        self.click(self._UPLOAD_EXCEL_BUTTON)

    def click_cancel_changes_button(self):
        self.click(self._CANCEL_ADDING_BUTTON)

    def click_add_changes_button(self):
        self.click(self._ADD_CHANGES_BUTTON)

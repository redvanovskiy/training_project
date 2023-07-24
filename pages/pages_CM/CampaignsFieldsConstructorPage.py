import time
import random
from random import randint
import string

from base.base import Base
from selenium.webdriver.common.by import By


class CampaignsFieldsConstructorPage(Base):

    _LOGIN_INPUT = (By.CSS_SELECTOR, "#principal")
    _PASSWORD_INPUT = (By.CSS_SELECTOR, "#credential")
    _SIGN_IN_BUTTON = (By.CSS_SELECTOR, ".ant-row-middle .ant-btn-primary")

    _FIELDS_CONSTRUCTOR_BUTTON = (By.CSS_SELECTOR, ".ant-btn.const-btn")
    _ADD_CAMPAIGN_BUTTON = (By.CSS_SELECTOR, ".campaigns__table .campaigns__table-btns button")
    _UCCX_UCCE_BUTTON = (By.CSS_SELECTOR, ".campaigns__table .campaigns__table-btns li:nth-child(1)")
    _GMSU_BUTTON = (By.CSS_SELECTOR, ".campaigns__table .campaigns__table-btns li:nth-child(2)")
    _CAMPAIGN_NAME_INPUT = (By.CSS_SELECTOR, ".add-campaign__row-el:nth-child(1) .ant-input")
    _CODE_INPUT = (By.CSS_SELECTOR, ".add-campaign__row-el:nth-child(2) .ant-input")
    _CAMPAIGN_PREFIX_INPUT = (By.CSS_SELECTOR, ".add-campaign__row-el:nth-child(3) .ant-input")
    _DEALER_MODE_SELECTOR = (By.CSS_SELECTOR, ".add-campaign__row-el:nth-child(4) .ant-select")
    _INBOUND_MODE = (By.CSS_SELECTOR, "")
    _PREDICTIVEONLY_MODE = (By.CSS_SELECTOR, "")
    _PREVIEWONLY_MODE = (By.CSS_SELECTOR, "")
    _PROGRESSIVEONLY_MODE = (By.CSS_SELECTOR, "")
    _PREVIEWDIRECTONLY_MODE = (By.CSS_SELECTOR, "")
    _CISCO_CAMPAIGN_DN_SELECTOR = (By.CSS_SELECTOR, ".add-campaign__row-el:nth-child(5) .ant-select")
    _ABANDON = (By.CSS_SELECTOR, "")
    _SAME_TIME_NEXT_BUSINESS_DAY = (By.CSS_SELECTOR, "")
    _USE_CAMPAIGN_DN = (By.CSS_SELECTOR, "")
    _CAMPAIGN_TYPE_SELECTOR = (By.CSS_SELECTOR, ".add-campaign__row-el:nth-child(6) .ant-select")
    _AGENT_TYPE = (By.CSS_SELECTOR, "")
    _IVR_TYPE = (By.CSS_SELECTOR, "")
    _COMMENT_INPUT = (By.CSS_SELECTOR, ".add-campaign__row:nth-child(2) .add-campaign__row-el .ant-input")
    _TIME_ZONE_SELECTOR = (By.CSS_SELECTOR, ".add-campaign__row:nth-child(2) .add-campaign__row-el:nth-child(2) .ant-select-selector")
    _FIRST_TIME_ZONE = (By.CSS_SELECTOR, "")
    _SKILL_GROUP_SELECTOR = (By.CSS_SELECTOR, ".add-campaign__row:nth-child(2) .add-campaign__row-el:nth-child(3) .ant-select-selector")
    _FIRST_SKILL_GROUP = (By.CSS_SELECTOR, "")
    _CANCEL_BUTTON = (By.CSS_SELECTOR, ".add-campaign__row:nth-child(2) .add-campaign__btns .ant-btn:nth-child(1)")
    _ADD_BUTTON = (By.CSS_SELECTOR, ".add-campaign__row:nth-child(2) .add-campaign__btns .ant-btn:nth-child(2)")

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


    def click_add_campaign_button(self):
        self.click(self._ADD_CAMPAIGN_BUTTON)

    def click_uccx_ucce_button(self):
        self.click(self._UCCX_UCCE_BUTTON)

    def click_gmsu_button(self):
        self.click(self._GMSU_BUTTON)

    def set_campaign_name(self, campaign_name):
        self.send_keys(self._CAMPAIGN_NAME_INPUT, campaign_name)

    def set_random_campaign_name(self, length):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))

    def set_code(self, code):
        self.send_keys(self._CODE_INPUT, code)

    def set_campaign_prefix(self, code):
        self.send_keys(self._CAMPAIGN_PREFIX_INPUT, code)

    def open_dialer_mode_selector(self):
        self.click(self._DEALER_MODE_SELECTOR)

    def select_inbound_mode(self):
        self.click(self._INBOUND_MODE)

    def select_predictiveonly_mode(self):
        self.click(self._PREDICTIVEONLY_MODE)

    def select_previewonly_mode(self):
        self.click(self._PREVIEWONLY_MODE)

    def select_progressiveonly_mode(self):
        self.click(self._PROGRESSIVEONLY_MODE)

    def select_previewdirectonly_mode(self):
        self.click(self._PREVIEWDIRECTONLY_MODE)

    def open_cisco_campaign_dn_selector(self):
        self.click(self._CISCO_CAMPAIGN_DN_SELECTOR)

    def select_abandon(self):
        self.click(self._ABANDON)

    def select_same_time_next_business_day(self):
        self.click(self._SAME_TIME_NEXT_BUSINESS_DAY)

    def select_use_campaign_dn(self):
        self.click(self._USE_CAMPAIGN_DN)

    def open_campaign_type_selector(self):
        self.click(self._CAMPAIGN_TYPE_SELECTOR)

    def select_agent_type(self):
        self.click(self._AGENT_TYPE)

    def select_ivr(self):
        self.click(self._IVR_TYPE)

    def set_comment(self, comment):
        self.send_keys(self._COMMENT_INPUT, comment)

    def set_random_comment(self, length):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))

    def open_time_zone_selector(self):
        self.click(self._TIME_ZONE_SELECTOR)

    def select_first_time_zone(self):
        self.click(self._FIRST_TIME_ZONE)

    def open_skill_group_selector(self):
        self.click(self._SKILL_GROUP_SELECTOR)

    def select_first_skill_group(self):
        self.click(self._FIRST_SKILL_GROUP)

    def click_cancel_button(self):
        self.click(self._CANCEL_BUTTON)

    def click_add_button(self):
        self.click(self._ADD_BUTTON)









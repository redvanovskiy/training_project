from base.base import Base
from selenium.webdriver.common.by import By


class CampaignsPage(Base):

    _LOGIN_INPUT = (By.CSS_SELECTOR, "#principal")
    _PASSWORD_INPUT = (By.CSS_SELECTOR, "#credential")
    _SIGN_IN_BUTTON = (By.CSS_SELECTOR, ".ant-row-middle .ant-btn-primary")

    _CAMPAIGNS_TAB = (By.CSS_SELECTOR, ".ant-tabs-nav-list :nth-child(5)")
    _CLIENT_GROUP_FILTER = (By.CSS_SELECTOR, ".cell--wrapper--clientGroup button")
    _UCCE_CHECKBOX = (By.CSS_SELECTOR, ".cell--wrapper--clientGroup ._dropdown_search label:nth-child(1) .ant-checkbox-input")
    _UCCX_CHECKBOX = (By.CSS_SELECTOR, ".cell--wrapper--clientGroup ._dropdown_search label:nth-child(2) .ant-checkbox-input")
    _GMSU_CHECKBOX = (By.CSS_SELECTOR, ".cell--wrapper--clientGroup ._dropdown_search label:nth-child(3) .ant-checkbox-input")
    _STATUS_FILTER = (By.CSS_SELECTOR, ".cell--wrapper--status button")
    _NOT_READY_CHECKBOX = (By.CSS_SELECTOR, ".cell--wrapper--status ._dropdown_search label:nth-child(1) .ant-checkbox-input")
    _ADDING_ABONENTS_CHECKBOX = (By.CSS_SELECTOR, ".cell--wrapper--status ._dropdown_search label:nth-child(2) .ant-checkbox-input")
    _READY_CHECKBOX = (By.CSS_SELECTOR, ".cell--wrapper--status ._dropdown_search label:nth-child(3) .ant-checkbox-input")
    _STARTING_CHECKBOX = (By.CSS_SELECTOR, ".cell--wrapper--status ._dropdown_search label:nth-child(4) .ant-checkbox-input")
    _IN_PROGRESS_CHECKBOX = (By.CSS_SELECTOR, ".cell--wrapper--status ._dropdown_search label:nth-child(5) .ant-checkbox-input")
    _GETTING_RESULT_CHECKBOX = (By.CSS_SELECTOR, ".cell--wrapper--status ._dropdown_search label:nth-child(6) .ant-checkbox-input")

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

    def open_campaigns_tab(self):
        self.click(self._CAMPAIGNS_TAB)

    def open_client_group_filter(self):
        self.click(self._CLIENT_GROUP_FILTER)

    def filter_client_group_by_ucce(self):
        self.click(self._UCCE_CHECKBOX)

    def filter_client_group_by_uccx(self):
        self.click(self._UCCX_CHECKBOX)

    def filter_client_group_by_gmsu(self):
        self.click(self._GMSU_CHECKBOX)

    def open_status_filter(self):
        self.click(self._STATUS_FILTER)

    def filter_status_by_not_ready(self):
        self.click(self._NOT_READY_CHECKBOX)

    def filter_status_by_adding_abonents(self):
        self.click(self._ADDING_ABONENTS_CHECKBOX)

    def filter_status_by_ready(self):
        self.click(self._READY_CHECKBOX)

    def filter_status_by_starting(self):
        self.click(self._STARTING_CHECKBOX)

    def filter_status_by_in_progress(self):
        self.click(self._IN_PROGRESS_CHECKBOX)

    def filter_status_by_getting_result(self):
        self.click(self._GETTING_RESULT_CHECKBOX)




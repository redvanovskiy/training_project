from pages.orangeHRM.LoginPage import LoginPage
from pages.orangeHRM.MainPage import MainPage
from pages.orangeHRM.PIMPage import PIMPage


class BaseClass:

    driver = None
    page = None
    login = None
    pim = None
    found_text = '(1) Record Found'

    @classmethod
    def setup_class(cls):
        cls.login = LoginPage(cls.driver)
        cls.page = MainPage(cls.driver)
        cls.pim = PIMPage(cls.driver)
        cls.page.open()


class TestCRUDEmployee(BaseClass):

    def setup_method(self):
        # Refresh page before new test
        self.page.refresh()

    def test_success_add_new_employee(self):
        self.login._login('Admin', 'admin123')
        self.page.visible(self.page._SEARCH_FIELD)
        self.page.click(self.page._PIM_BUTTON)
        self.pim.add_employee()
        self.pim.visible(self.pim._SUCCESS_ALERT)

    def test_success_search_employee(self):
        self.page.click(self.page._PIM_BUTTON)
        self.pim.send_keys(self.pim._EMPLOYEE_NAME_SEARCH_FIELD, "Raut")
        self.pim.click(self.pim._SEARCH_BUTTON)
        self.pim.assert_text(self.pim._TITLE_RECORD_FOUND, self.found_text)

    def test_not_success_search_employee(self):
        self.page.click(self.page._PIM_BUTTON)
        self.pim.send_keys(self.pim._EMPLOYEE_NAME_SEARCH_FIELD, self.pim.cred+self.pim.cred)
        self.pim.click(self.pim._SEARCH_BUTTON)
        self.pim.visible(self.pim._INFO_ALERT)

    def test_success_edit_employee(self):
        self.page.click(self.page._PIM_BUTTON)
        self.pim.send_keys(self.pim._EMPLOYEE_NAME_SEARCH_FIELD, self.pim.cred)
        self.pim.click(self.pim._SEARCH_BUTTON)
        self.pim.click(self.pim._EDIT_BUTTON)
        self.pim.visible(self.pim._EMPLOYEE_IMAGE)
        self.pim.send_keys(self.pim._LAST_NAME_FIELD, "1")
        self.pim.click(self.pim._SAVE_BUTTON)
        self.pim.visible(self.pim._SUCCESS_ALERT)

    def test_success_delete_employee(self):
        self.page.click(self.page._PIM_BUTTON)
        self.pim.send_keys(self.pim._EMPLOYEE_NAME_SEARCH_FIELD, self.pim.cred)
        self.pim.click(self.pim._SEARCH_BUTTON)
        self.pim.click(self.pim._DELETE_BUTTON)
        self.pim.click(self.pim._ACCEPT_DELETE)
        self.pim.visible(self.pim._SUCCESS_ALERT)

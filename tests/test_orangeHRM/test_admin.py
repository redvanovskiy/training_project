from pages.orangeHRM.LoginPage import LoginPage
from pages.orangeHRM.MainPage import MainPage
from pages.orangeHRM.PIMPage import PIMPage
from pages.orangeHRM.AdminPage import AdminPage
import time


class BaseClass:

    driver = None
    page = None
    login = None
    pim = None
    admin = None

    @classmethod
    def setup_class(cls):
        cls.login = LoginPage(cls.driver)
        cls.page = MainPage(cls.driver)
        cls.pim = PIMPage(cls.driver)
        cls.admin = AdminPage(cls.driver)
        cls.page.open()


class TestAdmin(BaseClass):

    def setup_method(self):
        # Refresh page before new test
        self.page.refresh()

    def test_success_add_new_employee(self):
        self.login._login('Admin', 'admin123')
        self.page.visible(self.page._SEARCH_FIELD)
        self.page.click(self.page._PIM_BUTTON)
        self.pim.add_employee()
        self.page.visible(self.pim._SUCCESS_ALERT)

    def test_employee_changes_to_admin(self):
        self.page.click(self.page._ADMIN_BUTTON)
        self.page.click(self.admin._ADD_BUTTON)
        self.page.click(self.admin._USER_ROLE_FIELD)
        self.page.click(self.admin._USER_ROLE_ADMIN)
        self.page.click(self.admin._STATUS_FIELD)
        self.page.click(self.admin._STATUS_ENABLED)
        self.page.send_keys(self.admin._EMPLOYEE_NAME, self.pim.cred)
        time.sleep(1)
        self.page.click(self.admin._EMPLOYEE_LISTBOX)
        self.page.send_keys(self.admin._NAME_FIELD, self.admin._username)
        self.page.send_keys(self.admin._PASSWORD_FIELD, self.admin._password)
        self.page.send_keys(self.admin._CONFIRM_PASSWORD, self.admin._password)
        self.page.click(self.admin._SAVE_BUTTON)
        self.page.visible(self.admin._LOADER)

    def test_new_admin_login(self):
        self.login.click_logout_button()
        self.page.visible(self.login._LOGIN_BUTTON)
        self.login._login(self.admin._username, self.admin._password)
        self.page.visible(self.login._USER_MENU)
import time

from pages.pages_orangehrm.LoginPage import LoginPage


class BaseClass:

    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        cls.page = LoginPage(cls.driver)
        cls.page.open()


class TestLogin(BaseClass):

    def setup_method(self):
        # Refresh page before new test
        self.page.refresh()

    def test_failed_login_with_empty_credentials(self):
        self.page._login('', '')
        self.page.check_required_login()
        self.page.check_required_password()

    def test_failed_login_with_empty_username(self):
        self.page._login('', 'admin123')
        self.page.check_required_login()

    def test_failed_login_with_empty_password(self):
        self.page._login('Admin', '')
        self.page.check_required_password()

    def test_failed_login_with_incorrect_username(self):
        self.page._login('neAdmin', 'admin123')
        self.page.check_invalid_credentials_message()

    def test_failed_login_with_incorrect_password(self):
        self.page._login('Admin', 'admin1234')
        self.page.check_invalid_credentials_message()

    def test_successful_login(self):
        self.page._login('Admin', 'admin123')
        time.sleep(2)
        self.page.visible(self.page._USER_PROFILE)

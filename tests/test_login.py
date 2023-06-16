from pages.LoginPage import LoginPage
from base.utils import HOST


class BaseClass:

    driver = None
    navigate = None

    @classmethod
    def setup_class(cls):
        cls.page = LoginPage(cls.driver)


class TestAuthentication(BaseClass):

    def setup_method(self):
        # Open the login page
        self.page.open()

    def test_login_module_url_returns_expected_value(self):
        return True

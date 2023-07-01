from pages.pages_orangehrm.LoginPage import LoginPage


class BaseClass:

    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        cls.page = LoginPage(cls.driver)
        cls.page.open()


class TestLogout(BaseClass):

    def setup_method(self):
        # Refresh page before new test
        self.page.refresh()

    def test_logout(self):
        # Clear cookies for logout
        self.page.driver.delete_all_cookies()
        self.page.refresh()
        # Run test
        self.page._login('Admin', 'admin123')
        self.page.visible(self.page._USER_PROFILE)
        self.page.open_user_dropdown()
        self.page.click_logout_button()
        self.page.visible(self.page._LOGIN_BUTTON)

from pages.orangeHRM.LoginPage import LoginPage


class BaseClass:

    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        cls.page = LoginPage(cls.driver)
        cls.page.open()


class TestLogin(BaseClass):

    forgot_message = 'Please enter your username to identify your account to reset your password'
    failed_msg = 'Invalid credentials'

    def setup_method(self):
        # Refresh page before new test
        self.page.refresh()

    def test_failed_login_with_empty_credentials(self):
        self.page._login('', '')
        self.page.visible(self.page._LOGIN_INPUT_ERROR)
        self.page.visible(self.page._REQUIRED_MESSAGE_LOGIN)
        self.page.visible(self.page._PASSWORD_INPUT_ERROR)
        self.page.visible(self.page._REQUIRED_MESSAGE_PASSWORD)

    def test_failed_login_with_empty_username(self):
        self.page._login('', 'admin123')
        self.page.visible(self.page._LOGIN_INPUT_ERROR)
        self.page.visible(self.page._REQUIRED_MESSAGE_LOGIN)

    def test_failed_login_with_empty_password(self):
        self.page._login('Admin', '')
        self.page.visible(self.page._PASSWORD_INPUT_ERROR)
        self.page.visible(self.page._REQUIRED_MESSAGE_PASSWORD)

    def test_failed_login_with_incorrect_username(self):
        self.page._login('Admin_fail', 'admin123')
        self.page.assert_text(self.page._ALERT_TEXT, self.failed_msg)

    def test_failed_login_with_incorrect_password(self):
        self.page._login('Admin', '1234')
        self.page.assert_text(self.page._ALERT_TEXT, self.failed_msg)

    def test_successful_login(self):
        self.page._login('Admin', 'admin123')
        self.page.visible(self.page._USER_MENU)

    def test_successful_logout(self):
        # Clear cookies for logout
        self.page.driver.delete_all_cookies()
        self.page.refresh()
        # Run test
        self.page._login('Admin', 'admin123')
        self.page.visible(self.page._USER_MENU)
        self.page.click_logout_button()
        self.page.visible(self.page._LOGIN_BUTTON)

    def test_reset_password_page(self):
        self.page.click(self.page._FORGOT_PASSWORD_BUTTON)
        self.page.assert_text(self.page._FORGOT_PASSWORD_PAGE, self.forgot_message)
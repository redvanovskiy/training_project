from pages.pages__demoblaze.LoginPage import LoginPage


class BaseClass:

    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        cls.page = LoginPage(cls.driver)
        cls.page.open()


class TestLogin(BaseClass):

    fail_msg = 'Please fill out Username and Password.'
    doesnt_exist_msg = 'User does not exist.'
    wrong_pass_msg = 'Wrong password.'

    def setup_method(self):
        # Refresh page before new test
        self.page.refresh()

    def test_failed_login_with_empty_credentials(self):
        self.page._login('', '')
        self.page.assert_text_in_alert(self.fail_msg)
        self.page.accept_alert()

    def test_failed_login_with_empty_username(self):
        self.page._login('', '1234567890')
        self.page.assert_text_in_alert(self.fail_msg)
        self.page.accept_alert()

    def test_failed_login_with_empty_password(self):
        self.page._login('sm_john_doe', '')
        self.page.assert_text_in_alert(self.fail_msg)
        self.page.accept_alert()

    def test_failed_login_with_incorrect_username(self):
        self.page._login('sm_john_doe_fail', '1234567890')
        self.page.assert_text_in_alert(self.doesnt_exist_msg)
        self.page.accept_alert()

    def test_failed_login_with_incorrect_password(self):
        self.page._login('sm_john_doe', '1234')
        self.page.assert_text_in_alert(self.wrong_pass_msg)
        self.page.accept_alert()

    def test_successful_login(self):
        self.page._login('sm_john_doe', '1234567890')
        self.page.visible(self.page._LOGOUT_BUTTON)

    def test_successful_logout(self):
        # Clear cookies for logout
        self.page.driver.delete_all_cookies()
        self.page.refresh()
        # Run test
        self.page._login('sm_john_doe', '1234567890')
        self.page.visible(self.page._LOGOUT_BUTTON)
        self.page.click_logout_button()
        self.page.visible(self.page._LOGIN_BUTTON)

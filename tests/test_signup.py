from pages.SignupPage import SignupPage
from pages.LoginPage import LoginPage
import random
import string


class BaseClass:

    driver = None
    page = None
    login = None


    @classmethod
    def setup_class(cls):
        cls.page = SignupPage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.page.open()
        cls.login.open()


class TestSignup(BaseClass):

    fail_msg = 'Please fill out Username and Password.'
    user_exist = 'This user already exist.'
    sign_up_ok = 'Sign up successful.'
    user_name = ''.join(random.choice(string.ascii_letters) for i in range(10))

    def setup_method(self):
        # Refresh page before new test
        self.page.refresh()

    def test_successful_signup(self):
        self.page.click_signup_button()
        self.page.set_username(self.user_name)
        self.page.set_password('1')
        self.page.click_submit_signup_button()
        self.login.assert_text_in_alert(self.sign_up_ok)
        self.login.accept_alert()

    # def test_failed_login_with_empty_credentials(self):
    #     self.page._login('', '')
    #     self.page.assert_text_in_alert(self.fail_msg)
    #     self.page.accept_alert()
    #
    # def test_failed_login_with_empty_username(self):
    #     self.page._login('', '1234567890')
    #     self.page.assert_text_in_alert(self.fail_msg)
    #     self.page.accept_alert()
    #
    # def test_failed_login_with_empty_password(self):
    #     self.page._login('sm_john_doe', '')
    #     self.page.assert_text_in_alert(self.fail_msg)
    #     self.page.accept_alert()
    #
    # def test_failed_login_with_incorrect_username(self):
    #     self.page._login('sm_john_doe_fail', '1234567890')
    #     self.page.assert_text_in_alert(self.doesnt_exist_msg)
    #     self.page.accept_alert()
    #
    # def test_failed_login_with_incorrect_password(self):
    #     self.page._login('sm_john_doe', '1234')
    #     self.page.assert_text_in_alert(self.wrong_pass_msg)
    #     self.page.accept_alert()
    #

    #
    # def test_successful_logout(self):
    #     # Clear cookies for logout
    #     self.page.driver.delete_all_cookies()
    #     self.page.refresh()
    #     # Run test
    #     self.page._login('sm_john_doe', '1234567890')
    #     self.page.visible(self.page._LOGOUT_BUTTON)
    #     self.page.click_logout_button()
    #     self.page.visible(self.page._LOGIN_BUTTON)
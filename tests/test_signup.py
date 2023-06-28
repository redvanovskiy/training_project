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
    cred = ''.join(random.choice(string.ascii_letters) for i in range(10))

    def setup_method(self):
        # Refresh page before new test
        self.page.refresh()

    def test_successful_signup(self):
        self.page._signup(self.cred, self.cred)
        self.login.assert_text_in_alert(self.sign_up_ok)
        self.login.accept_alert()

    def test_failed_signup_with_empty_credentials(self):
        self.page._signup('', '')
        self.login.assert_text_in_alert(self.fail_msg)
        self.login.accept_alert()

    def test_failed_signup_with_user_exist(self):
        self.page._signup('1', '1')
        self.login.assert_text_in_alert(self.user_exist)
        self.login.accept_alert()

    def test_failed_signup_with_empty_username(self):
        self.page._signup('', self.cred)
        self.login.assert_text_in_alert(self.fail_msg)
        self.login.accept_alert()

    def test_failed_signup_with_empty_password(self):
        self.page._signup(self.cred, '')
        self.login.assert_text_in_alert(self.fail_msg)
        self.login.accept_alert()

    def test_successful_signup_and_login_logout(self):
        # Clear cookies for logout
        self.page.driver.delete_all_cookies()
        self.page.refresh()
        # Run test
        loc_cred = ''.join(random.choice(string.ascii_letters) for i in range(10))
        self.page._signup(loc_cred, loc_cred)
        self.login.assert_text_in_alert(self.sign_up_ok)
        self.login.accept_alert()
        self.page.refresh()
        self.login._login(loc_cred, loc_cred)
        self.page.visible(self.login._LOGOUT_BUTTON)
        self.login.click_logout_button()
        self.page.visible(self.login._LOGIN_BUTTON)
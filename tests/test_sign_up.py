from pages.Sign_upPage import Sign_upPage


class BaseClass:

    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        cls.page = Sign_upPage(cls.driver)
        cls.page.open()

class TestSign_up(BaseClass):

    fail_msg = 'Please fill out Username and Password.'
    another_fail_msg = 'This user already exist.'
    successful_msg = 'Sign up successful.'

    def setup_method(self):
        # Refresh page before new test
        self.page.refresh()

    def test_failed_sign_up_with_empty_credentials(self):
        self.page._sign_up('', '')
        self.page.assert_text_in_alert(self.fail_msg)
        self.page.accept_alert()

    def test_failed_sign_up_with_space_credentials(self):
        self.page._sign_up(' ', ' ')
        self.page.assert_text_in_alert(self.another_fail_msg)
        self.page.accept_alert()

    def test_failed_sign_up_with_empty_username(self):
        self.page._sign_up('', '12345qwerty')
        self.page.assert_text_in_alert(self.fail_msg)
        self.page.accept_alert()

    def test_failed_sign_up_with_space_username(self):
        self.page._sign_up(' ', '12345qwerty')
        self.page.assert_text_in_alert(self.another_fail_msg)
        self.page.accept_alert()

    def test_failed_sign_up_with_empty_password(self):
        self.page._sign_up('toster', '')
        self.page.assert_text_in_alert(self.fail_msg)
        self.page.accept_alert()

    def test_failed_sign_up_with_already_exist_user(self):
        self.page._sign_up('tostercomposter', 'tostercomposter')
        self.page.assert_text_in_alert(self.another_fail_msg)
        self.page.accept_alert()

    def test_successful_sign_up(self):
        self.page._sign_up('toster', '12345qwerty')
        self.page.assert_text_in_alert(self.successful_msg)

    def test_successful_random_sign_up(self):
        self.page._sign_up(self.page.set_random_username, self.page.set_random_password)
        self.page.assert_text_in_alert(self.successful_msg)

from pages.demoblaze.HomePage import HomePage
from pages.demoblaze.LoginPage import LoginPage
from pages.demoblaze.AboutUsPage import AboutUsPage
from pages.demoblaze.ContactFormPage import ContactFormPage
from pages.demoblaze.ProductPage import ProductPage
from pages.demoblaze.SignupPage import SignupPage

class BaseClass:

    driver = None
    page = None
    login = None
    home = None
    form = None
    about = None
    sign = None

    @classmethod
    def setup_class(cls):
        cls.page = ProductPage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.home = HomePage(cls.driver)
        cls.form = ContactFormPage(cls.driver)
        cls.about = AboutUsPage(cls.driver)
        cls.sign = SignupPage(cls.driver)

class TestMainMenu(BaseClass):

    def setup_method(self):
        # About Us page open and clear cookies before new test
        self.page.driver.delete_all_cookies()
        self.page.refresh()
        self.page.open()

    def test_about_us_page_is_open(self):
        self.page.click(self.home._ABOUT_US)
        self.page.visible(self.about._START_PLAY_BUTTON)

    def test_contact_form_page_is_open(self):
        self.page.click(self.home._CONTACT)
        self.page.visible(self.form._SEND_MESSAGE_BUTTON)

    def test_cart_page_is_open(self):
        self.page.click(self.home._CART)
        self.page.visible(self.page._PLACE_ORDER_BUTTON)

    def test_log_in_page_is_open(self):
        self.page.click(self.login._LOGIN_BUTTON)
        self.page.visible(self.login._SUBMIT_LOGIN_BUTTON)

    def test_sign_up_page_is_open(self):
        self.page.click(self.login._SIGNUP_BUTTON)
        self.page.visible(self.sign._SUBMIT_SIGNUP_BUTTON)

    def test_home_button_is_work(self):
        self.page.click(self.home._CART)
        self.page.visible(self.page._PLACE_ORDER_BUTTON)
        self.page.click(self.home._HOME_BUTTON)
        self.page.visible(self.home._CAROUSEL)
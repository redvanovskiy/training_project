from pages.demoblaze.HomePage import HomePage
from pages.demoblaze.LoginPage import LoginPage
from pages.demoblaze.ProductPage import ProductPage
import time


class BaseClass:

    driver = None
    page = None
    login = None
    home = None
    product_name = 'Samsung galaxy s6'
    product_price = '$360 *includes tax'
    product_description = 'The Samsung Galaxy S6 is powered by 1.5GHz octa-core Samsung Exynos 7420 processor and it comes with 3GB of RAM. The phone packs 32GB of internal storage cannot be expanded.'

    @classmethod
    def setup_class(cls):
        cls.page = ProductPage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.home = HomePage(cls.driver)
        cls.page.open()


class TestProduct(BaseClass):

    def setup_method(self):
        # Home page open before new test
        self.page.open()
        self.home.click_product_page()

    def test_assert_name(self):
        self.page.assert_product_name(self.product_name)
        self.page.visible(self.page._ADD_TO_CART_BUTTON)

    def test_assert_price(self):
        self.page.assert_product_price(self.product_price)
        self.page.visible(self.page._ADD_TO_CART_BUTTON)

    def test_assert_description(self):
        self.page.assert_product_description(self.product_description)
        self.page.visible(self.page._ADD_TO_CART_BUTTON)


class TestProductUser(BaseClass):

    def setup_method(self):
        # Home page open before new test
        self.page.open()
        self.login._login('1', '1')
        time.sleep(1)
        self.home.click_product_page()

    def test_assert_name(self):
        self.page.assert_product_name(self.product_name)
        self.login.visible(self.login._LOGOUT_BUTTON)

    def test_assert_price(self):
        self.page.assert_product_price(self.product_price)
        self.login.visible(self.login._LOGOUT_BUTTON)

    def test_assert_description(self):
        self.page.assert_product_description(self.product_description)
        self.page.visible(self.page._ADD_TO_CART_BUTTON)

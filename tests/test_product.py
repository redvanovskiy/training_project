from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.ProductPage import ProductPage


class BaseClass:

    driver = None
    page = None
    login = None
    home = None


    @classmethod
    def setup_class(cls):
        cls.page = ProductPage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.home = HomePage(cls.driver)
        cls.page.open()

class TestProduct(BaseClass):

    product_name = 'Samsung galaxy s6'
    product_price = '$360 *includes tax'

    def setup_method(self):
        # Home page open before new test
        self.page.open()

    def test_assert_name(self):
        self.home.click_product_page()
        self.page.assert_product_name(self.product_name)
        self.page.visible(self.page._ADD_TO_CART_BUTTON)

    def test_assert_price(self):
        self.home.click_product_page()
        self.page.assert_product_price(self.product_price)
        self.page.visible(self.page._ADD_TO_CART_BUTTON)

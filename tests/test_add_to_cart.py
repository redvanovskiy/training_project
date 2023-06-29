from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.ProductPage import ProductPage
import time

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

    product_added = 'Product added'

    def setup_method(self):
        # Home page open before new test
        self.page.driver.delete_all_cookies()
        self.page.refresh()
        self.page.open()
        self.home.click_product_page()

    def test_cart_page_is_opened(self):
        self.home.click_cart()
        self.page.visible(self.page._PRODUCT_NAME_PAGE)

    def test_product_added_to_cart(self):
        self.page.click(self.page._ADD_TO_CART_BUTTON)
        self.login.assert_text_in_alert(self.product_added)
        self.login.accept_alert()

    def test_product_added_to_cart_full(self):
        self.page.click(self.page._ADD_TO_CART_BUTTON)
        self.login.assert_text_in_alert(self.product_added)
        self.login.accept_alert()
        self.home.click_cart()
        self.page.visible(self.page._DELETE_BUTTON_OF_PRODUCT)

    def test_a_few_product_added_to_cart(self):
        self.page.click(self.page._ADD_TO_CART_BUTTON)
        self.login.assert_text_in_alert(self.product_added)
        self.login.accept_alert()
        self.home.click_cart()
        self.page.visible(self.page._DELETE_BUTTON_OF_PRODUCT)
        self.page.click(self.home._HOME_BUTTON)
        self.home.click_product_page_1()
        self.page.click(self.page._ADD_TO_CART_BUTTON)
        self.login.assert_text_in_alert(self.product_added)
        self.login.accept_alert()
        self.home.click_cart()
        self.page.visible(self.page._DELETE_BUTTON_OF_PRODUCT_1)

    def test_delete_product_from_cart(self):
        self.page.click(self.page._ADD_TO_CART_BUTTON)
        self.login.assert_text_in_alert(self.product_added)
        self.login.accept_alert()
        self.home.click_cart()
        self.page.delete_product()


class TestProduct_user(BaseClass):

    product_added = 'Product added.'

    def setup_method(self):
        # Home page open before new test
        self.page.open()
        self.login._login('1', '1')
        time.sleep(1)
        self.home.click_product_page()

    def test_cart_page_is_opened(self):
        self.home.click_cart()
        self.page.visible(self.page._PRODUCT_NAME_PAGE)

    def test_product_added_to_cart(self):
        self.page.click(self.page._ADD_TO_CART_BUTTON)
        self.login.assert_text_in_alert(self.product_added)
        self.login.accept_alert()

    def test_delete_product_from_cart(self):
        self.home.click_cart()
        self.page.visible(self.page._DELETE_BUTTON_OF_PRODUCT)
        time.sleep(1)
        self.page.delete_product()

    def test_product_full_added_to_cart(self):
        self.page.click(self.page._ADD_TO_CART_BUTTON)
        self.login.assert_text_in_alert(self.product_added)
        self.login.accept_alert()
        self.home.click_cart()
        self.page.visible(self.page._DELETE_BUTTON_OF_PRODUCT)
        self.page.delete_product()

    def test_a_few_product_added_to_cart(self):
        self.page.click(self.page._ADD_TO_CART_BUTTON)
        self.login.assert_text_in_alert(self.product_added)
        self.login.accept_alert()
        self.home.click_cart()
        self.page.visible(self.page._DELETE_BUTTON_OF_PRODUCT)
        self.page.click(self.home._HOME_BUTTON)
        self.home.click_product_page_1()
        self.page.click(self.page._ADD_TO_CART_BUTTON)
        self.login.assert_text_in_alert(self.product_added)
        self.login.accept_alert()
        self.home.click_cart()
        self.page.visible(self.page._DELETE_BUTTON_OF_PRODUCT)
        self.page.delete_product()
        time.sleep(1)
        self.page.visible(self.page._DELETE_BUTTON_OF_PRODUCT)
        self.page.delete_product()
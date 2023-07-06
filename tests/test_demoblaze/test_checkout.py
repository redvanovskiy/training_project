from pages.demoblaze.HomePage import HomePage
from pages.demoblaze.LoginPage import LoginPage
from pages.demoblaze.ProductPage import ProductPage
from pages.demoblaze.CheckoutPage import CheckoutPage
import time


class BaseClass:

    driver = None
    page = None
    login = None
    home = None
    check = None
    fail_mes = 'Please fill out Name and Creditcard.'
    product_added = 'Product added'
    product_added_user = 'Product added.'

    @classmethod
    def setup_class(cls):
        cls.page = ProductPage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.home = HomePage(cls.driver)
        cls.check = CheckoutPage(cls.driver)


class TestCheckoutWithoutProductsIncognito(BaseClass):

    def setup_method(self):
        # Home page open and clear cookies before new test
        self.page.driver.delete_all_cookies()
        self.page.refresh()
        self.page.open()
        self.home.click_product_page()
        self.home.click_cart()

    def test_place_order_is_open(self):
        self.page.click(self.page._PLACE_ORDER_BUTTON)
        self.page.visible(self.check._PLACE_ORDER_TITLE)

    def test_place_order_can_be_closed_button(self):
        self.page.click(self.page._PLACE_ORDER_BUTTON)
        self.page.visible(self.check._PLACE_ORDER_TITLE)
        self.page.click(self.check._CLOSE_BUTTON)

    def test_place_order_can_be_closed_icon(self):
        self.page.click(self.page._PLACE_ORDER_BUTTON)
        self.page.visible(self.check._PLACE_ORDER_TITLE)
        self.page.click(self.check._CLOSE_ICON)

    def test_purchase_without_products_and_filling_fields(self):
        self.page.click(self.page._PLACE_ORDER_BUTTON)
        self.page.visible(self.check._PLACE_ORDER_TITLE)
        self.page.click(self.check._PURCHASE_BUTTON)
        self.login.assert_text_in_alert(self.fail_mes)
        self.login.accept_alert()

    def test_purchase_without_products_but_fill_creditcard_field(self):
        self.page.click(self.page._PLACE_ORDER_BUTTON)
        self.page.visible(self.check._PLACE_ORDER_TITLE)
        self.page.send_keys(self.check._CREDIT_CARD_INPUT, self.check.cred)
        self.page.click(self.check._PURCHASE_BUTTON)
        self.login.assert_text_in_alert(self.fail_mes)
        self.login.accept_alert()

    def test_success_purchase_without_products_but_fill_name_and_creditcard_fields(self):
        self.page.click(self.page._PLACE_ORDER_BUTTON)
        self.page.visible(self.check._PLACE_ORDER_TITLE)
        self.page.send_keys(self.check._NAME_INPUT, self.check.cred)
        self.page.send_keys(self.check._CREDIT_CARD_INPUT, self.check.cred)
        self.page.click(self.check._PURCHASE_BUTTON)
        self.page.visible(self.check._SUCCESS_TITLE)
        self.page.click(self.check._OK_BUTTON)


class TestCheckoutWithProductsIncognito(BaseClass):

    def setup_method(self):
        # Home page open and clear cookies before new test
        self.page.driver.delete_all_cookies()
        self.page.refresh()
        self.page.open()
        self.home.click_product_page()
        self.page.click(self.page._ADD_TO_CART_BUTTON)
        self.login.assert_text_in_alert(self.product_added)
        self.login.accept_alert()
        self.home.click_cart()
        self.page.click(self.page._PLACE_ORDER_BUTTON)

    def test_purchase_with_products_but_without_filling_fields(self):

        self.page.click(self.check._PURCHASE_BUTTON)
        self.login.assert_text_in_alert(self.fail_mes)
        self.login.accept_alert()

    def test_purchase_with_products_and_fill_name_field_but_without_creditcard_field(self):
        self.page.send_keys(self.check._NAME_INPUT, self.check.cred)
        self.page.click(self.check._PURCHASE_BUTTON)
        self.login.assert_text_in_alert(self.fail_mes)
        self.login.accept_alert()

    def test_success_purchase_fill_all_fields(self):
        self.page.send_keys(self.check._NAME_INPUT, self.check.cred)
        self.page.send_keys(self.check._CREDIT_CARD_INPUT, self.check.cred)
        self.page.send_keys(self.check._COUNTRY_INPUT, self.check.cred)
        self.page.send_keys(self.check._CITY_INPUT, self.check.cred)
        self.page.send_keys(self.check._MONTH_INPUT, '04')
        self.page.send_keys(self.check._YEAR_INPUT, '2000')
        self.page.click(self.check._PURCHASE_BUTTON)
        self.page.visible(self.check._SUCCESS_TITLE)
        self.page.click(self.check._OK_BUTTON)

    def test_success_purchase_fill_name_and_creditcard_fields(self):
        self.page.send_keys(self.check._NAME_INPUT, self.check.cred)
        self.page.send_keys(self.check._CREDIT_CARD_INPUT, self.check.cred)
        self.page.click(self.check._PURCHASE_BUTTON)
        self.page.visible(self.check._SUCCESS_TITLE)
        self.page.click(self.check._OK_BUTTON)


class TestCheckoutWithoutProductsUser(BaseClass):

    def setup_method(self):
        # Home page open and clear cookies before new test
        self.page.driver.delete_all_cookies()
        self.page.refresh()
        self.page.open()
        self.login._login('1', '1')
        time.sleep(1)
        self.home.click_product_page()
        self.home.click_cart()

    def test_place_order_is_open(self):
        self.page.click(self.page._PLACE_ORDER_BUTTON)
        self.page.visible(self.check._PLACE_ORDER_TITLE)

    def test_place_order_can_be_closed_button(self):
        self.page.click(self.page._PLACE_ORDER_BUTTON)
        self.page.visible(self.check._PLACE_ORDER_TITLE)
        self.page.click(self.check._CLOSE_BUTTON)

    def test_place_order_can_be_closed_icon(self):
        self.page.click(self.page._PLACE_ORDER_BUTTON)
        self.page.visible(self.check._PLACE_ORDER_TITLE)
        self.page.click(self.check._CLOSE_ICON)

    def test_purchase_without_products_and_filling_fields(self):
        self.page.click(self.page._PLACE_ORDER_BUTTON)
        self.page.visible(self.check._PLACE_ORDER_TITLE)
        self.page.click(self.check._PURCHASE_BUTTON)
        self.login.assert_text_in_alert(self.fail_mes)
        self.login.accept_alert()

    def test_purchase_without_products_but_fill_creditcard_field(self):
        self.page.click(self.page._PLACE_ORDER_BUTTON)
        self.page.visible(self.check._PLACE_ORDER_TITLE)
        self.page.send_keys(self.check._CREDIT_CARD_INPUT, self.check.cred)
        self.page.click(self.check._PURCHASE_BUTTON)
        self.login.assert_text_in_alert(self.fail_mes)
        self.login.accept_alert()

    def test_success_purchase_without_products_but_fill_name_and_creditcard_fields(self):
        self.page.click(self.page._PLACE_ORDER_BUTTON)
        self.page.visible(self.check._PLACE_ORDER_TITLE)
        self.page.send_keys(self.check._NAME_INPUT, self.check.cred)
        self.page.send_keys(self.check._CREDIT_CARD_INPUT, self.check.cred)
        self.page.click(self.check._PURCHASE_BUTTON)
        self.page.visible(self.check._SUCCESS_TITLE)
        self.page.click(self.check._OK_BUTTON)


class TestCheckoutWithProductsUser(BaseClass):

    def setup_method(self):
        # Home page open and clear cookies before new test
        self.page.driver.delete_all_cookies()
        self.page.refresh()
        self.page.open()
        self.login._login('1', '1')
        time.sleep(1)
        self.home.click_product_page()
        self.page.click(self.page._ADD_TO_CART_BUTTON)
        self.login.assert_text_in_alert(self.product_added_user)
        self.login.accept_alert()
        self.home.click_cart()
        self.page.click(self.page._PLACE_ORDER_BUTTON)

    def test_purchase_with_products_but_without_filling_fields(self):

        self.page.click(self.check._PURCHASE_BUTTON)
        self.login.assert_text_in_alert(self.fail_mes)
        self.login.accept_alert()
        self.page.click(self.check._CLOSE_BUTTON)
        self.page.delete_product()

    def test_purchase_with_products_and_fill_name_field_but_without_creditcard_field(self):
        self.page.send_keys(self.check._NAME_INPUT, self.check.cred)
        self.page.click(self.check._PURCHASE_BUTTON)
        self.login.assert_text_in_alert(self.fail_mes)
        self.login.accept_alert()
        self.page.click(self.check._CLOSE_BUTTON)
        self.page.delete_product()

    def test_success_purchase_fill_all_fields(self):
        self.page.send_keys(self.check._NAME_INPUT, self.check.cred)
        self.page.send_keys(self.check._CREDIT_CARD_INPUT, self.check.cred)
        self.page.send_keys(self.check._COUNTRY_INPUT, self.check.cred)
        self.page.send_keys(self.check._CITY_INPUT, self.check.cred)
        self.page.send_keys(self.check._MONTH_INPUT, '04')
        self.page.send_keys(self.check._YEAR_INPUT, '2000')
        self.page.click(self.check._PURCHASE_BUTTON)
        self.page.visible(self.check._SUCCESS_TITLE)
        self.page.click(self.check._OK_BUTTON)

    def test_success_purchase_fill_name_and_creditcard_fields(self):
        self.page.send_keys(self.check._NAME_INPUT, self.check.cred)
        self.page.send_keys(self.check._CREDIT_CARD_INPUT, self.check.cred)
        self.page.click(self.check._PURCHASE_BUTTON)
        self.page.visible(self.check._SUCCESS_TITLE)
        self.page.click(self.check._OK_BUTTON)

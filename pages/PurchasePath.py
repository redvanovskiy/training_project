import time

from base.base import Base
from selenium.webdriver.common.by import By


class PurchasePath(Base):

    _LOGIN_BUTTON = (By.CSS_SELECTOR, "#login2")
    _LOGIN_INPUT = (By.CSS_SELECTOR, "#loginusername")
    _PASSWORD_INPUT = (By.CSS_SELECTOR, "#loginpassword")
    _SUBMIT_LOGIN_BUTTON = (By.CSS_SELECTOR, "#logInModal .btn.btn-primary")
    _NAME_OF_USER = (By.CSS_SELECTOR, "#nameofuser")
    _PRODUCT_1 = (By.PARTIAL_LINK_TEXT, "Samsung galaxy s6")
    _PRODUCT_2 = (By.PARTIAL_LINK_TEXT, "Nexus 6")
    _ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn.btn-success.btn-lg")
    success_msg = 'Product added'
    _CART_BUTTON = (By.CSS_SELECTOR, "#cartur")
    _HOME_BUTTON = (By.CSS_SELECTOR, ".nav-item.active .nav-link")
    _DELETE_BUTTON = (By.CSS_SELECTOR, "#tbodyid .success:nth-of-type(1) :nth-of-type(4) a")
    _PLACE_ORDER_BUTTON = (By.CSS_SELECTOR, ".btn.btn-success")
    _NAME = (By.CSS_SELECTOR, "#name")
    _COUNTRY = (By.CSS_SELECTOR, "#country")
    _CITY = (By.CSS_SELECTOR, "#city")
    _CREDIT_CARD = (By.CSS_SELECTOR, "#card")
    _MONTH = (By.CSS_SELECTOR, "#month")
    _YEAR = (By.CSS_SELECTOR, "#year")
    _CLOSE_BUTTON = (By.CSS_SELECTOR, "#orderModal .modal-footer .btn.btn-secondary")
    _PURCHASE_BUTTON = (By.CSS_SELECTOR, "#orderModal .modal-footer .btn.btn-primary")
    _THANK_MESSAGE = (By.CSS_SELECTOR, ".sweet-alert.showSweetAlert.visible :nth-child(6)")
    _CONFIRM_BUTTON = (By.CSS_SELECTOR, ".showSweetAlert .confirm")

    def __init__(self, driver):
        super().__init__(driver)

    def click_login_button(self):
        self.click(self._LOGIN_BUTTON)

    def set_username(self, username):
        self.send_keys(self._LOGIN_INPUT, username)

    def set_password(self, password):
        self.send_keys(self._PASSWORD_INPUT, password)

    def click_submit_login_button(self):
        self.click(self._SUBMIT_LOGIN_BUTTON)

    def login(self, username, password):
        self.click_login_button()
        self.set_username(username)
        self.set_password(password)
        self.click_submit_login_button()

    def open_product_page(self):
        self.click(self._PRODUCT_1)

    def click_add_to_cart_button(self):
        self.click(self._ADD_TO_CART_BUTTON)

    def assert_text_in_alert(self, expected_text):
        time.sleep(2)
        alert = self.driver.switch_to.alert
        assert str(alert.text) == str(expected_text)

    def accept_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def back_to_home_page(self):
        self.click(self._HOME_BUTTON)

    def open_cart(self):
        self.click(self._CART_BUTTON)

    def click_delete_button(self):
        self.click(self._DELETE_BUTTON)

    def click_place_order_button(self):
        self.click(self._PLACE_ORDER_BUTTON)

    def set_name(self, username):
        self.send_keys(self._NAME, username)

    def set_country(self, country):
        self.send_keys(self._COUNTRY, country)

    def set_city(self, city):
        self.send_keys(self._CITY, city)

    def set_credit_card(self, credit_card):
        self.send_keys(self._CREDIT_CARD, credit_card)

    def set_month(self, month):
        self.send_keys(self._MONTH, month)

    def set_year(self, year):
        self.send_keys(self._YEAR, year)

    def click_close_button(self):
        self.click(self._CLOSE_BUTTON)

    def click_purchase_button(self):
        self.click(self._PURCHASE_BUTTON)

    def click_ok_button(self):
        self.click(self._CONFIRM_BUTTON)

    def choice_of_goods(self):
        self.click(self._PRODUCT_1)
        self.click_add_to_cart_button()
        self.assert_text_in_alert(self.success_msg)
        self.accept_alert()
        self.back_to_home_page()
        time.sleep(2)
        self.click(self._PRODUCT_2)
        self.click_add_to_cart_button()
        self.assert_text_in_alert(self.success_msg)
        self.accept_alert()
        self.open_cart()
        time.sleep(2)
        self.click_delete_button()
        time.sleep(2)

    def set_credential(self, username, country, city, credit_card, month, year):
        self.click_place_order_button()
        self.set_name(username)
        self.set_country(country)
        self.set_city(city)
        self.set_credit_card(credit_card)
        self.set_month(month)
        self.set_year(year)

    def confirm_payment_and_check_receipt(self):
        self.click_purchase_button()
        self.visible(self._THANK_MESSAGE)
        self.click_ok_button()

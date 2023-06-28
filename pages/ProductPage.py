from base.base import Base
from selenium.webdriver.common.by import By


class ProductPage(Base):
    _ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#tbodyid > div.row > div > a")
    _PRODUCT_IMAGE = (By.CSS_SELECTOR, "#imgp > div > img")
    _PRODUCT_NAME = (By.CSS_SELECTOR, "#tbodyid > h2")
    _PRODUCT_PRICE = (By.CSS_SELECTOR, "#tbodyid > h3")

    def __init__(self, driver):
        super().__init__(driver)

    def assert_product_name(self, expected_text):
        self.assert_text(self._PRODUCT_NAME, expected_text)

    def assert_product_price(self, expected_text):
        self.assert_text(self._PRODUCT_PRICE, expected_text)

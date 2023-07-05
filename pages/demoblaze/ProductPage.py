from base.base import Base
from selenium.webdriver.common.by import By


class ProductPage(Base):
    _ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#tbodyid > div.row > div > a")
    _PRODUCT_IMAGE = (By.CSS_SELECTOR, "#imgp > div > img")
    _PRODUCT_NAME = (By.CSS_SELECTOR, "#tbodyid > h2")
    _PRODUCT_PRICE = (By.CSS_SELECTOR, "#tbodyid > h3")
    _PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, '#more-information > p')
    _PRODUCT_NAME_PAGE = (By.CSS_SELECTOR, '#page-wrapper > div > div.col-lg-8 > h2')
    _DELETE_BUTTON_OF_PRODUCT = (By.CSS_SELECTOR, '#tbodyid > tr > td:nth-child(4) > a')
    _DELETE_BUTTON_OF_PRODUCT_1 = (By.CSS_SELECTOR, '#tbodyid > tr:nth-child(2) > td:nth-child(4) > a')
    _PLACE_ORDER_BUTTON = (By.CSS_SELECTOR, '#page-wrapper > div > div.col-lg-1 > button')

    def __init__(self, driver):
        super().__init__(driver)

    def assert_product_name(self, expected_text):
        self.assert_text(self._PRODUCT_NAME, expected_text)

    def assert_product_price(self, expected_text):
        self.assert_text(self._PRODUCT_PRICE, expected_text)

    def assert_product_description(self, expected_text):
        self.assert_text(self._PRODUCT_DESCRIPTION, expected_text)

    def assert_product_name_page(self, expected_text):
        self.assert_text(self._PRODUCT_NAME_PAGE, expected_text)

    def delete_product(self):
        self.click(self._DELETE_BUTTON_OF_PRODUCT)
from pages.demoblaze.HomePage import HomePage
from pages.demoblaze.ProductPage import ProductPage
import time


class BaseClass:

    driver = None
    page = None
    home = None

    @classmethod
    def setup_class(cls):
        cls.page = ProductPage(cls.driver)
        cls.home = HomePage(cls.driver)
        cls.page.open()


class TestPaginations(BaseClass):

    def setup_method(self):
        # Refresh page open before new test
        self.page.refresh()
        time.sleep(1)

    def test_paginations_button_is_present(self):
        self.page.visible(self.home._NEXT_BUTTON)
        self.page.visible(self.home._PREVIOUS_BUTTON)

    def test_next_button_is_work(self):
        self.page.click(self.home._NEXT_BUTTON)
        self.page.visible(self.home._PRODUCT_MONITOR)

    def test_previous_button_is_work(self):
        self.page.click(self.home._NEXT_BUTTON)
        self.page.not_visible(self.home._PRODUCT_LAPTOP)
        self.page.visible(self.home._PRODUCT_MONITOR)
        self.page.click(self.home._PREVIOUS_BUTTON)
        self.page.visible(self.home._PRODUCT_LAPTOP)

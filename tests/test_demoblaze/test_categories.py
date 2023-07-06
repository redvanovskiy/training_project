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


class TestCategories(BaseClass):

    def setup_method(self):
        # Refresh page open before new test
        self.page.refresh()
        time.sleep(1)

    def test_laptops_page_is_open(self):
        self.page.click(self.home._LAPTOP_BUTTON)
        self.page.visible(self.home._PRODUCT_LAPTOP)

    def test_monitors_page_is_open(self):
        self.page.click(self.home._MONITORS_BUTTON)
        self.page.visible(self.home._PRODUCT_MONITOR)

    def test_phones_page_is_open(self):
        self.page.click(self.home._PHONES_BUTTON)
        self.page.not_visible(self.home._PRODUCT_LAPTOP)

    def test_categories_button_is_work(self):
        self.page.click(self.home._LAPTOP_BUTTON)
        self.page.visible(self.home._PRODUCT_LAPTOP)
        self.page.click(self.home._CATEGORIES)
        self.page.visible(self.home._PRODUCT_LAPTOP)
        self.page.visible(self.home._PRODUCT_PHONE)
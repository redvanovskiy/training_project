from base.base import Base
from selenium.webdriver.common.by import By


class HomePage(Base):
    _NAVBAR = (By.CSS_SELECTOR, "#navbarExample")
    _CAROUSEL = (By.CSS_SELECTOR, "#carouselExampleIndicators")
    _CATEGORIES = (By.CSS_SELECTOR, "#contcont .list-group ")
    _PRODUCTS = (By.CSS_SELECTOR, "#contcont #tbodyid")
    _PAGINATION = (By.CSS_SELECTOR, "#prev2")
    _FOOTER = (By.CSS_SELECTOR, "#footc #fotcont")
    _CONTACT = (By.CSS_SELECTOR, "#navbarExample li:nth-child(2)")
    _ABOUT_US = (By.CSS_SELECTOR, "#navbarExample li:nth-child(3)")
    _PRODUCT_PHONE = (By.PARTIAL_LINK_TEXT, "Samsung galaxy s6")
    _PRODUCT_LAPTOP = (By.PARTIAL_LINK_TEXT, "Sony vaio i7")
    _PRODUCT_MONITOR = (By.PARTIAL_LINK_TEXT, "Apple monitor 24")
    _CART = (By.CSS_SELECTOR,"#cartur")
    _HOME_BUTTON = (By.CSS_SELECTOR, "#navbarExample li:nth-child(1)")
    _PHONES_BUTTON = (By.CSS_SELECTOR, ".list-group .list-group-item:nth-of-type(2)")
    _LAPTOP_BUTTON = (By.CSS_SELECTOR, ".list-group .list-group-item:nth-of-type(3)")
    _MONITORS_BUTTON = (By.CSS_SELECTOR, ".list-group .list-group-item:nth-of-type(4)")
    _NEXT_BUTTON = (By.CSS_SELECTOR, "#next2")
    _PREVIOUS_BUTTON = (By.CSS_SELECTOR, "#prev2")

    def __init__(self, driver):
        super().__init__(driver)

    def click_product_page(self):
        self.click(self._PRODUCT_PHONE)

    def click_cart(self):
        self.click(self._CART)

    def click_product_page_1(self):
        self.click(self._PRODUCT_LAPTOP)

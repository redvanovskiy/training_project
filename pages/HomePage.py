from base.base import Base
from selenium.webdriver.common.by import By


class HomePage(Base):
    _NAVBAR = (By.CSS_SELECTOR, "#navbarExample")
    _CAROUSEL = (By.CSS_SELECTOR, "#carouselExampleIndicators")
    _CATEGORIES = (By.CSS_SELECTOR, "#contcont .list-group ")
    _PRODUCTS = (By.CSS_SELECTOR, "#contcont #tbodyid")
    _PAGINATION = (By.CSS_SELECTOR, "#prev2")
    _FOOTER = (By.CSS_SELECTOR, "#footc #fotcont")
    _PRODUCT_PAGE_1 = (By.CSS_SELECTOR, "#tbodyid > div:nth-child(1) > div > a > img")
    _PRODUCT_PAGE_2 = (By.CSS_SELECTOR, '#tbodyid > div:nth-child(9) > div > div > h4 > a')
    _CART = (By.CSS_SELECTOR,"#cartur")
    _HOME_BUTTON = (By.CSS_SELECTOR, '#navbarExample > ul > li.nav-item.active > a')


    def __init__(self, driver):
        super().__init__(driver)

    def click_product_page(self):
        self.click(self._PRODUCT_PAGE_1)

    def click_cart(self):
        self.click(self._CART)

    def click_product_page_1(self):
        self.click(self._PRODUCT_PAGE_2)

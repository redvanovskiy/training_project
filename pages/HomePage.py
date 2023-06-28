from base.base import Base
from selenium.webdriver.common.by import By


class HomePage(Base):
    _NAVBAR = (By.CSS_SELECTOR, "#navbarExample")
    _CAROUSEL = (By.CSS_SELECTOR, "#carouselExampleIndicators")
    _CATEGORIES = (By.CSS_SELECTOR, "#contcont .list-group ")
    _PRODUCTS = (By.CSS_SELECTOR, "#contcont #tbodyid")
    _PAGINATION = (By.CSS_SELECTOR, "#prev2")
    _FOOTER = (By.CSS_SELECTOR, "#footc #fotcont")
    _PRODUCT_PAGE = (By.CSS_SELECTOR,"#tbodyid > div:nth-child(1) > div > a > img")

    def __init__(self, driver):
        super().__init__(driver)

    def click_product_page(self):
        self.click(self._PRODUCT_PAGE)

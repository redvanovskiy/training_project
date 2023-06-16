from base.base import Base
from selenium.webdriver.common.by import By


class HomePage(Base):
    _NAVBAR = (By.CSS_SELECTOR, "#navbarExample")
    _CAROUSEL = (By.CSS_SELECTOR, "#carouselExampleIndicators")
    _CATEGORIES = (By.CSS_SELECTOR, "#contcont .list-group ")
    _PRODUCTS = (By.CSS_SELECTOR, "#contcont #tbodyid")
    _PAGINATION = (By.CSS_SELECTOR, "#prev2")
    _FOOTER = (By.CSS_SELECTOR, "#footc #fotcont")

    def __init__(self, driver):
        super().__init__(driver)

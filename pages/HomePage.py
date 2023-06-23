from base.base import Base
from selenium.webdriver.common.by import By


class HomePage(Base):

    _NAVBAR = (By.CSS_SELECTOR, "#navbarExample")
    _ABOUT_US = (By.CSS_SELECTOR,"#videoModal")
    _CAROUSEL = (By.CSS_SELECTOR, "#carouselExampleIndicators")
    _CAROUSEL_CONTROL_PREV = (By.CSS_SELECTOR, ".carousel-control-prev-icon")
    _CAROUSEL_CONTROL_NEXT = (By.CSS_SELECTOR, ".carousel-control-next-icon")
    _CAROUSEL_CONTROL_TAB = (By.CSS_SELECTOR, "#carouselExampleIndicators .carousel-indicators :not(.active)")
    _CATEGORIES = (By.CSS_SELECTOR, "#contcont .list-group ")
    _CATEGORIES_NAME = (By.CSS_SELECTOR, "#contcont .list-group #itemc")
    _1CATEGORIES_NAME = (By.CSS_SELECTOR, ".list-group .list-group-item:nth-of-type(1)")
    _2CATEGORIES_NAME = (By.CSS_SELECTOR, ".list-group .list-group-item:nth-of-type(2)")
    _3CATEGORIES_NAME = (By.CSS_SELECTOR, ".list-group .list-group-item:nth-of-type(3)")
    _PRODUCTS = (By.CSS_SELECTOR, "#contcont #tbodyid")
    _PRODUCT1 = (By.PARTIAL_LINK_TEXT, "Nokia lumia 1520")
    _PRODUCT2 = (By.PARTIAL_LINK_TEXT, "ASUS Full HD")
    _PAGINATION_PREV = (By.CSS_SELECTOR, "#prev2")
    _PAGINATION_NEXT = (By.CSS_SELECTOR, "#frm #next2")
    _FOOTER = (By.CSS_SELECTOR, "#footc #fotcont")

    def __init__(self, driver):
        super().__init__(driver)

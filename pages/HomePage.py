from base.base import Base
from selenium.webdriver.common.by import By


class HomePage(Base):
    _NAVBAR = (By.CSS_SELECTOR, "#navbarExample")
    _ABOUT_US = (By.CSS_SELECTOR,"#videoModal")
    _CAROUSEL = (By.CSS_SELECTOR, "#carouselExampleIndicators")
    _CAROUSEL_CONTROL_PREV = (By.CSS_SELECTOR, ".carousel-control-prev-icon")
    _CAROUSEL_CONTROL_NEXT = (By.CSS_SELECTOR, ".carousel-control-next-icon")
    _CAROUSEL_CONTROL_TAB = (By.CSS_SELECTOR, "#carouselExampleIndicators .carousel-indicators .active")
    # _CAROUSEL_CONTROL_TAB = (By.CSS_SELECTOR, "#carouselExampleIndicators .carousel-indicators > li[data-slide-to=\"2\"]")
    _CATEGORIES = (By.CSS_SELECTOR, "#contcont .list-group ")
    _CATEGORIES_NAME = (By.CSS_SELECTOR, "#contcont .list-group #itemc")
    _1CATEGORIES_NAME = (By.CSS_SELECTOR, "#contcont .list-group > a[onclick=\"byCat('phone')\"]")
    _2CATEGORIES_NAME = (By.XPATH, "/html/body/div[5]/div/div[1]/div/a[3]")
    _3CATEGORIES_NAME = (By.XPATH, "/html/body/div[5]/div/div[1]/div/a[4]")
    _PRODUCTS = (By.CSS_SELECTOR, "#contcont #tbodyid")
    _PAGINATION_PREV = (By.CSS_SELECTOR, "#prev2")
    _PAGINATION_NEXT = (By.CSS_SELECTOR, "#frm #next2")

    _FOOTER = (By.CSS_SELECTOR, "#footc #fotcont")

    def __init__(self, driver):
        super().__init__(driver)

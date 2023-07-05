from base.base import Base
from selenium.webdriver.common.by import By


class HomePage(Base):
    _NAVBAR = (By.CSS_SELECTOR, "#navbarExample")
    _CAROUSEL = (By.CSS_SELECTOR, "#carouselExampleIndicators")
    _CATEGORIES = (By.CSS_SELECTOR, "#contcont .list-group ")
    _PRODUCTS = (By.CSS_SELECTOR, "#contcont #tbodyid")
    _PAGINATION = (By.CSS_SELECTOR, "#prev2")
    _FOOTER = (By.CSS_SELECTOR, "#footc #fotcont")
    _CONTACT = (By.CSS_SELECTOR, '#navbarExample > ul > li:nth-child(2) > a')
    _ABOUT_US = (By.CSS_SELECTOR, '#navbarExample > ul > li:nth-child(3) > a')
    _PRODUCT_PHONE = (By.CSS_SELECTOR, "#tbodyid > div:nth-child(1) > div > a > img")
    _PRODUCT_LAPTOP = (By.CSS_SELECTOR, '#tbodyid > div:nth-child(9) > div > div > h4 > a')
    _PRODUCT_MONITOR = (By.CSS_SELECTOR, '#tbodyid > div:nth-child(1) > div > div > h4 > a')
    _CART = (By.CSS_SELECTOR,"#cartur")
    _HOME_BUTTON = (By.CSS_SELECTOR, '#navbarExample > ul > li.nav-item.active > a')
    _LAPTOP_BUTTON = (By.XPATH, '/html/body/div[5]/div/div[1]/div/a[3]')
    _MONITORS_BUTTON = (By.XPATH, '/html/body/div[5]/div/div[1]/div/a[4]')
    _PHONES_BUTTON = (By.XPATH, '/html/body/div[5]/div/div[1]/div/a[2]')
    _NEXT_BUTTON = (By.CSS_SELECTOR, '#next2')
    _PREVIOUS_BUTTON = (By.CSS_SELECTOR, '#prev2')


    def __init__(self, driver):
        super().__init__(driver)

    def click_product_page(self):
        self.click(self._PRODUCT_PHONE)

    def click_cart(self):
        self.click(self._CART)

    def click_product_page_1(self):
        self.click(self._PRODUCT_LAPTOP)

from base.base import Base
from selenium.webdriver.common.by import By


class ProductPage(Base):
    _PLACE_ORDER_TITLE = (By.CSS_SELECTOR, "#orderModalLabel")
    _NAME_INPUT = (By.CSS_SELECTOR, "#name")
    _COUNTRY_INPUT = (By.CSS_SELECTOR, "#country")
    _CITY_INPUT = (By.CSS_SELECTOR, "#city")
    _CREDIT_CARD_INPUT = (By.CSS_SELECTOR, '#card')
    _MONTH_INPUT = (By.CSS_SELECTOR, '#month')
    _YEAR_INPUT = (By.CSS_SELECTOR, '#year')
    _CLOSE_BUTTON = (By.CSS_SELECTOR, '#orderModal > div > div > div.modal-footer > button.btn.btn-secondary')
    _PURCHASE_BUTTON = (By.CSS_SELECTOR, '#orderModal > div > div > div.modal-footer > button.btn.btn-primary')

    def __init__(self, driver):
        super().__init__(driver)
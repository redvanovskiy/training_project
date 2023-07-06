from base.base import Base
from selenium.webdriver.common.by import By
import random
import string


class CheckoutPage(Base):
    _PLACE_ORDER_TITLE = (By.CSS_SELECTOR, "#orderModalLabel")
    _NAME_INPUT = (By.CSS_SELECTOR, "#name")
    _COUNTRY_INPUT = (By.CSS_SELECTOR, "#country")
    _CITY_INPUT = (By.CSS_SELECTOR, "#city")
    _CREDIT_CARD_INPUT = (By.CSS_SELECTOR, "#card")
    _MONTH_INPUT = (By.CSS_SELECTOR, "#month")
    _YEAR_INPUT = (By.CSS_SELECTOR, "#year")
    _CLOSE_BUTTON = (By.CSS_SELECTOR, "#orderModal .modal-footer .btn-secondary")
    _PURCHASE_BUTTON = (By.CSS_SELECTOR, "#orderModal .modal-footer .btn-primary")
    _CLOSE_ICON = (By.CSS_SELECTOR, "#orderModal .modal-header .close")
    _SUCCESS_TITLE = (By.CSS_SELECTOR, " .sweet-alert.showSweetAlert.visible h2")
    _OK_BUTTON = (By.CSS_SELECTOR, " .sweet-alert .sa-confirm-button-container")
    cred = ''.join(random.choice(string.hexdigits) for i in range(10))

    def __init__(self, driver):
        super().__init__(driver)
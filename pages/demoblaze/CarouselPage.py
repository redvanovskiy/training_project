from base.base import Base
from selenium.webdriver.common.by import By


class CarouselPage(Base):
    _FIRST_SLIDE = (By.CSS_SELECTOR, "#carouselExampleIndicators :nth-child(1) > img")
    _SECOND_SLIDE = (By.CSS_SELECTOR, "#carouselExampleIndicators :nth-child(2) > img")
    _THIRD_SLIDE = (By.CSS_SELECTOR, "#carouselExampleIndicators :nth-child(3) > img")
    _FIRST_INDICATOR_ = (By.CSS_SELECTOR, '#carouselExampleIndicators [data-slide-to="0"]')
    _SECOND_INDICATOR = (By.CSS_SELECTOR, '#carouselExampleIndicators [data-slide-to="1"]')
    _THIRD_INDICATOR = (By.CSS_SELECTOR, '#carouselExampleIndicators [data-slide-to="2"]')
    _PREVIOUS_BUTTON = (By.CSS_SELECTOR, "#carouselExampleIndicators .carousel-control-prev-icon")
    _NEXT_BUTTON = (By.CSS_SELECTOR, '#carouselExampleIndicators .carousel-control-next-icon')

    def __init__(self, driver):
        super().__init__(driver)
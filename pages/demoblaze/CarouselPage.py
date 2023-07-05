from base.base import Base
from selenium.webdriver.common.by import By


class CarouselPage(Base):
    _FIRST_SLIDE = (By.XPATH, "/html/body/nav/div[2]/div/div/div[1]/img")
    _SECOND_SLIDE = (By.XPATH, "/html/body/nav/div[2]/div/div/div[2]/img")
    _THIRD_SLIDE = (By.XPATH, "/html/body/nav/div[2]/div/div/div[3]/img")
    _FIRST_INDICATOR_ = (By.XPATH, '/html/body/nav/div[2]/div/ol/li[1]')
    _SECOND_INDICATOR = (By.XPATH, '/html/body/nav/div[2]/div/ol/li[2]')
    _THIRD_INDICATOR = (By.XPATH, '/html/body/nav/div[2]/div/ol/li[3]')
    _PREVIOUS_BUTTON = (By.XPATH, "/html/body/nav/div[2]/div/a[1]/span[1]")
    _NEXT_BUTTON = (By.XPATH, '/html/body/nav/div[2]/div/a[2]/span[1]')

    def __init__(self, driver):
        super().__init__(driver)
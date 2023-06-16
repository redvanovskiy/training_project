import time

from base.base import Base
from selenium.webdriver.common.by import By


class AboutUsPage(Base):
    _ABOUT_US_BUTTON = (By.CSS_SELECTOR, "#videoModal")
    _PLAY_VIDEO_BUTTON = (By.CSS_SELECTOR, ".vjs-big-play-button")
    _VIDEO = (By.CSS_SELECTOR, "#example-video_html5_api")
    _CLOSE_BUTTON = (By.CSS_SELECTOR, "#videoModal .btn.btn-secondary")
    _DESCRIPTION = (By.CSS_SELECTOR, "#fotcont .caption p")

    def __init__(self, driver):
        super().__init__(driver)

    def click_about_us_button(self):
        self.click(self._ABOUT_US_BUTTON)

    def click_play_button(self):
        self.click(self._PLAY_VIDEO_BUTTON)

    def click_close_button(self):
        self.click(self._ABOUT_US_BUTTON)

    def _about_us(self):
        self.click_about_us_button()
        self.visible(self._VIDEO)
        self.click_play_button()
        time.sleep(3)
        self.click_close_button()

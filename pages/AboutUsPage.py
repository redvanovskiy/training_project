from base.base import Base
from selenium.webdriver.common.by import By


class AboutUsPage(Base):
    _TITLE = (By.CSS_SELECTOR, "#videoModalLabel")
    _CLOSE_BUTTON = (By.CSS_SELECTOR, "#videoModal > div > div > div.modal-footer > button")
    _CLOSE_ICON = (By.CSS_SELECTOR, "#videoModal > div > div > div.modal-header > button > span")
    _START_PLAY_BUTTON = (By.CSS_SELECTOR, '#example-video > button')
    _PLAY_BUTTON = (By.CSS_SELECTOR, '#example-video > div.vjs-control-bar > button.vjs-play-control.vjs-control.vjs-button.vjs-paused')
    _PAUSE_BUTTON = (By.CSS_SELECTOR, '#example-video > div.vjs-control-bar > button.vjs-play-control.vjs-control.vjs-button.vjs-playing')
    _VOLUME_BUTTON = (By.CSS_SELECTOR, "#example-video > div.vjs-control-bar > div.vjs-volume-panel.vjs-control.vjs-volume-panel-horizontal > button")
    _VOLUME_MUTE_BUTTON = (By.CSS_SELECTOR, '#example-video > div.vjs-control-bar > div.vjs-volume-panel.vjs-control.vjs-volume-panel-horizontal > button')
    _VOLUME_CONTROL = (By.CSS_SELECTOR, '#example-video > div.vjs-control-bar > div.vjs-volume-panel.vjs-control.vjs-volume-panel-horizontal > div')
    _PROGRESS_HOLDER = (By.CSS_SELECTOR, "#example-video > div.vjs-control-bar > div.vjs-progress-control.vjs-control > div")
    _PICTURE_IN_PICTURE_BUTTON = (By.CSS_SELECTOR, "#example-video > div.vjs-control-bar > button.vjs-picture-in-picture-control.vjs-control.vjs-button")
    _EXIT_PICTURE_IN_PICTURE_BUTTON = (By.CSS_SELECTOR, '#example-video > div.vjs-control-bar > button.vjs-picture-in-picture-control.vjs-control.vjs-button')
    _FULL_SCREEN_BUTTON = (By.CSS_SELECTOR, "#example-video > div.vjs-control-bar > button.vjs-fullscreen-control.vjs-control.vjs-button")
    _NO_FULL_SCREEN_BUTTON = (By.CSS_SELECTOR, '#example-video > div.vjs-control-bar > button.vjs-fullscreen-control.vjs-control.vjs-button')


    def __init__(self, driver):
        super().__init__(driver)
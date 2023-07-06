from base.base import Base
from selenium.webdriver.common.by import By


class AboutUsPage(Base):
    _TITLE = (By.CSS_SELECTOR, "#videoModalLabel")
    _CLOSE_BUTTON = (By.CSS_SELECTOR, "#videoModal .modal-footer .btn-secondary")
    _CLOSE_ICON = (By.CSS_SELECTOR, "#videoModal .modal-header .close")
    _START_PLAY_BUTTON = (By.CSS_SELECTOR, "#example-video .vjs-big-play-button")
    _PLAY_BUTTON = (By.CSS_SELECTOR, "#example-video .vjs-control-bar .vjs-play-control.vjs-paused")
    _PAUSE_BUTTON = (By.CSS_SELECTOR, "#example-video .vjs-control-bar .vjs-play-control.vjs-playing")
    _VOLUME_BUTTON = (By.CSS_SELECTOR, "#example-video .vjs-control-bar .vjs-mute-control.vjs-vol-3")
    _VOLUME_MUTE_BUTTON = (By.CSS_SELECTOR, '#example-video .vjs-control-bar .vjs-mute-control.vjs-vol-0')
    _PROGRESS_HOLDER = (By.CSS_SELECTOR, "#example-video .vjs-control-bar .vjs-progress-control.vjs-control")
    _PICTURE_IN_PICTURE_BUTTON = (By.CSS_SELECTOR, "#example-video .vjs-control-bar [title='Picture-in-Picture']")
    _EXIT_PICTURE_IN_PICTURE = (By.CSS_SELECTOR, "#example-video .vjs-control-bar [title='Exit Picture-in-Picture']")
    _FULL_SCREEN_BUTTON = (By.CSS_SELECTOR, "#example-video .vjs-control-bar [title='Fullscreen']")
    _NO_FULL_SCREEN_BUTTON = (By.CSS_SELECTOR, "#example-video .vjs-control-bar [title='Non-Fullscreen']")

    def __init__(self, driver):
        super().__init__(driver)
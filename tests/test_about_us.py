from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.AboutUsPage import AboutUsPage
from selenium.webdriver import ActionChains
import time

class BaseClass:

    driver = None
    page = None
    login = None
    home = None
    action = None
    title = 'About us'

    @classmethod
    def setup_class(cls):
        cls.page = AboutUsPage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.home = HomePage(cls.driver)
        cls.action = ActionChains(cls.driver)


class TestAboutUs(BaseClass):

    def setup_method(self):
        # About Us page open and clear cookies before new test
        self.page.driver.delete_all_cookies()
        self.page.refresh()
        self.page.open()
        self.page.click(self.home._ABOUT_US)

    def test_about_us_page_is_open(self):
        self.page.visible(self.page._START_PLAY_BUTTON)

    def test_close_button_is_work(self):
        self.page.click(self.page._CLOSE_BUTTON)
        self.page.visible(self.home._PRODUCTS)

    def test_close_icon_is_work(self):
        self.page.click(self.page._CLOSE_ICON)
        self.page.visible(self.home._PRODUCTS)

    def test_video_can_be_played(self):
        self.page.click(self.page._START_PLAY_BUTTON)
        self.page.visible(self.page._PAUSE_BUTTON)

    def test_video_can_be_paused(self):
        self.page.click(self.page._START_PLAY_BUTTON)
        self.page.visible(self.page._FULL_SCREEN_BUTTON)
        self.page.click(self.page._PAUSE_BUTTON)
        self.page.visible(self.page._PLAY_BUTTON)

    def test_video_can_be_played_after_pause(self):
        self.page.click(self.page._START_PLAY_BUTTON)
        self.page.visible(self.page._FULL_SCREEN_BUTTON)
        self.page.click(self.page._PAUSE_BUTTON)
        self.page.visible(self.page._PLAY_BUTTON)
        self.page.click(self.page._PLAY_BUTTON)
        self.page.visible(self.page._PAUSE_BUTTON)

    def test_video_can_be_full_screen_mode(self):
        self.page.click(self.page._START_PLAY_BUTTON)
        self.page.click(self.page._FULL_SCREEN_BUTTON)
        self.page.visible(self.page._NO_FULL_SCREEN_BUTTON)

    def test_video_can_be_exit_full_screen_mode(self):
        self.page.click(self.page._START_PLAY_BUTTON)
        self.page.click(self.page._FULL_SCREEN_BUTTON)
        self.page.visible(self.page._NO_FULL_SCREEN_BUTTON)
        self.page.click(self.page._NO_FULL_SCREEN_BUTTON)
        self.page.visible(self.page._FULL_SCREEN_BUTTON)

    def test_video_can_be_picture_in_picture_mode(self):
        self.page.click(self.page._START_PLAY_BUTTON)
        self.page.click(self.page._PICTURE_IN_PICTURE_BUTTON)
        self.page.visible(self.page._EXIT_PICTURE_IN_PICTURE_BUTTON)

    def test_video_can_be_exit_picture_in_picture_mode(self):
        self.page.click(self.page._START_PLAY_BUTTON)
        self.page.click(self.page._PICTURE_IN_PICTURE_BUTTON)
        self.page.visible(self.page._EXIT_PICTURE_IN_PICTURE_BUTTON)
        self.page.click(self.page._EXIT_PICTURE_IN_PICTURE_BUTTON)
        self.page.visible(self.page._PICTURE_IN_PICTURE_BUTTON)

    def test_volume_can_be_mute(self):
        self.page.click(self.page._START_PLAY_BUTTON)
        self.page.click(self.page._VOLUME_BUTTON)
        self.page.visible(self.page._VOLUME_MUTE_BUTTON)

    def test_volume_can_be_unmute(self):
        self.page.click(self.page._START_PLAY_BUTTON)
        self.page.click(self.page._VOLUME_BUTTON)
        self.page.visible(self.page._VOLUME_MUTE_BUTTON)
        self.page.click(self.page._VOLUME_MUTE_BUTTON)
        self.page.visible(self.page._VOLUME_BUTTON)

    # def test_change_volume(self):
    #     self.page.click(self.page._START_PLAY_BUTTON)
    #     self.page.hover_to(self.page._VOLUME_BUTTON)
    #     self.page.hover_to(self.page._VOLUME_CONTROL)
    #     # self.action.click_and_hold(self.page._VOLUME_CONTROL).move_by_offset(-2, 0).release()
    #     self.action.drag_and_drop_by_offset(self.page._VOLUME_CONTROL, -2, 0)

    def test_progres_holder_can_be_change(self):
        self.page.click(self.page._START_PLAY_BUTTON)
        self.page.hover_to(self.page._PROGRESS_HOLDER)
        self.page.click(self.page._PROGRESS_HOLDER)
        time.sleep(3)







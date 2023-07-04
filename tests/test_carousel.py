from pages.CarouselPage import CarouselPage
import time

class BaseClass:

    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        cls.page = CarouselPage(cls.driver)

class TestCarousel(BaseClass):

    def setup_method(self):
        # Home page open and clear cookies before new test
        self.page.driver.delete_all_cookies()
        self.page.refresh()
        self.page.open()

    def test_slides_change_on_their_own(self):
        self.page.visible(self.page._FIRST_SLIDE)
        time.sleep(3)
        self.page.visible(self.page._SECOND_SLIDE)
        time.sleep(3)
        self.page.visible(self.page._THIRD_SLIDE)

    def test_slides_change_by_button_next(self):
        self.page.visible(self.page._FIRST_SLIDE)
        self.page.click(self.page._NEXT_BUTTON)
        self.page.visible(self.page._SECOND_SLIDE)
        time.sleep(2)
        self.page.click(self.page._NEXT_BUTTON)
        self.page.visible(self.page._THIRD_SLIDE)

    def test_slides_change_by_button_previous(self):
        self.page.visible(self.page._FIRST_SLIDE)
        self.page.click(self.page._PREVIOUS_BUTTON)
        self.page.visible(self.page._THIRD_SLIDE)
        time.sleep(2)
        self.page.click(self.page._PREVIOUS_BUTTON)
        self.page.visible(self.page._SECOND_SLIDE)

    def test_slides_change_by_clicking_on_indicator(self):
        self.page.visible(self.page._FIRST_SLIDE)
        self.page.click(self.page._THIRD_INDICATOR)
        self.page.visible(self.page._THIRD_SLIDE)
        time.sleep(1)
        self.page.click(self.page._FIRST_INDICATOR_)
        self.page.visible(self.page._FIRST_SLIDE)
        time.sleep(1)
        self.page.click(self.page._SECOND_INDICATOR)
        self.page.visible(self.page._SECOND_SLIDE)
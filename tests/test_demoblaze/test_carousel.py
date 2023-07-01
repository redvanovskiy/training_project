from pages.pages__demoblaze.HomePage import HomePage


class BaseClass:
    
    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        cls.page = HomePage(cls.driver)
        cls.page.open()


class TestCarousel(BaseClass):

    def setup_method(self):
        # Refresh page before new test
        self.page.refresh()

    def test_carousel_is_presented(self):
        self.page.visible(self.page._CAROUSEL)

    def test_prev_slide(self):
        self.page.click(self.page._CAROUSEL_CONTROL_PREV)

    def test_next_slide(self):
        self.page.click(self.page._CAROUSEL_CONTROL_NEXT)

    def test_mini_tab(self):
        self.page.click(self.page._CAROUSEL_CONTROL_TAB)

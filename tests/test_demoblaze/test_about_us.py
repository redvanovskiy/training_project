from pages.pages__demoblaze.AboutUsPage import AboutUsPage


class BaseClass:

    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        cls.page = AboutUsPage(cls.driver)
        cls.page.open()


class TestAboutUs(BaseClass):

    def setup_method(self):
        # Refresh page before new test
        self.page.refresh()

    def test_about_us(self):
        self.page._about_us()

    def test_read_description(self):
        self.page.visible(self.page._DESCRIPTION)

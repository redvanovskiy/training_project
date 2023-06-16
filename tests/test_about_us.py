from pages.AboutUsPage import AboutUsPage


class BaseClass:

    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        cls.page = AboutUsPage(cls.driver)
        cls.page.open()


class CheckAboutUs(BaseClass):

    def test_about_us(self):
        self.page._about_us()

    def read_description(self):
        self.page.visible(self.page._DESCRIPTION)

from pages.HomePage import HomePage


class BaseClass:

    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        cls.page = HomePage(cls.driver)
        cls.page.open()


class TestHome(BaseClass):

    def test_home_page_url_returns_expected_value(self):
        assert 'https://www.demoblaze.com/index.html' == self.page.url()

    def test_navbar_is_presented(self):
        self.page.visible(self.page._NAVBAR)

    def test_carousel_is_presented(self):
        self.page.visible(self.page._CAROUSEL)

    def test_categories_is_presented(self):
        self.page.visible(self.page._CATEGORIES)

    def test_products_are_presented(self):
        self.page.visible(self.page._PRODUCTS)

    def test_pagination_is_presented(self):
        self.page.visible(self.page._PAGINATION)

    def test_footer_is_presented(self):
        self.page.visible(self.page._FOOTER)

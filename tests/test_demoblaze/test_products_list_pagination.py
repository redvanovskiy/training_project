from pages.pages__demoblaze.HomePage import HomePage


class BaseClass:

    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        cls.page = HomePage(cls.driver)
        cls.page.open()


class TestPagination(BaseClass):

    def setup_method(self):
        # Refresh page before new test
        self.page.refresh()

    def test_pagination(self):
        self.page.visible(self.page._PAGINATION_PREV)
        self.page.clickable(self.page._PAGINATION_PREV)
        self.page.visible(self.page._PAGINATION_NEXT)
        self.page.clickable(self.page._PAGINATION_NEXT)

    def test_pagination_changes(self):
        self.page.visible(self.page._PAGINATION_NEXT)
        self.page.click(self.page._PAGINATION_NEXT)
        self.page.visible(self.page._PRODUCT2)
        self.page.click(self.page._PAGINATION_PREV)
        self.page.visible(self.page._PRODUCT1)

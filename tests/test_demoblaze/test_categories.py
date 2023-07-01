from pages.pages__demoblaze.HomePage import HomePage


class BaseClass:

    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        cls.page = HomePage(cls.driver)
        cls.page.open()


class TestCategories(BaseClass):

    def setup_method(self):
        # Refresh page before new test
        self.page.refresh()

    def test_categories_is_presented(self):
        self.page.visible(self.page._CATEGORIES)

    def test_open_phones_page(self):
        self.page.click(self.page._1CATEGORIES_NAME)

    def test_open_laptops_page(self):
        self.page.click(self.page._2CATEGORIES_NAME)

    def test_open_monitors_page(self):
        self.page.click(self.page._3CATEGORIES_NAME)

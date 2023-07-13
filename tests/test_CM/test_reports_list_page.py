import time

from pages.pages_CM.ReportsListPage import ReportsListPage


class BaseClass:

    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        cls.page = ReportsListPage(cls.driver)
        cls.page.open()


class TestGroupListPage(BaseClass):

    def setup_method(self):
        # Refresh page before new test
        self.page.refresh()

    def test_open_reports_list(self):
        self.page._login('s.borysenko', 's.borysenko')
        self.page.open_reports_list_tab()

    def test_download_report(self):
        self.page.download_first_report()

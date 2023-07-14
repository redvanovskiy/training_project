import time

from pages.pages_CM.RequestsListPage import RequestsListPage


class BaseClass:

    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        cls.page = RequestsListPage(cls.driver)
        cls.page.open()


class TestGroupListPage(BaseClass):

    def setup_method(self):
        # Refresh page before new test
        self.page.refresh()

    def test_open_campaigns_list(self):
        self.page._login('s.borysenko', 's.borysenko')
        self.page.open_requests_list_tab()

    def test_sort_by_diallistid(self):
        self.page.sort_by_diallistid()
        time.sleep(1)
        self.page.sort_by_diallistid()

    def test_sort_by_requestid(self):
        self.page.sort_by_requestid()
        time.sleep(1)
        self.page.sort_by_requestid()

    def test_sort_by_requesttext(self):
        self.page.sort_by_requesttext()
        time.sleep(1)
        self.page.sort_by_requesttext()

    def test_sort_by_cd_callresult(self):
        self.page.sort_by_cd_callresult()
        time.sleep(1)
        self.page.sort_by_cd_callresult()

    def test_sort_by_requestdatetime(self):
        self.page.sort_by_requestdatetime()
        time.sleep(1)
        self.page.sort_by_requestdatetime()

    def test_sort_by_cd_callstatus(self):
        self.page.sort_by_cd_callstatus()
        time.sleep(1)
        self.page.sort_by_cd_callstatus()

    def test_sort_by_cd_callmade(self):
        self.page.sort_by_cd_callmade()
        time.sleep(1)
        self.page.sort_by_cd_callmade()

    def test_sort_by_success(self):
        self.page.sort_by_success()
        time.sleep(1)
        self.page.sort_by_success()

    def test_sort_by_age(self):
        self.page.sort_by_age()
        time.sleep(1)
        self.page.sort_by_age()

    def test_click_refresh_button(self):
        self.page.click_refresh_button()

    def test_download_excel(self):
        self.page.click_export_to_excel_button()

    def test_cansel_changes_displayed_columns(self):
        self.page.check_displayed_columns()
        self.page.select_age_column()
        self.page.select_cd_callresult_column()
        self.page.click_cansel_button()

    def test_change_displayed_columns(self):
        self.page.check_displayed_columns()
        self.page.select_cd_callstatus_column()
        self.page.select_requesttext_column()
        self.page.click_apply_button()

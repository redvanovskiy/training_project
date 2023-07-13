import time

from pages.pages_CM.CampaignsPage import CampaignsPage


class BaseClass:

    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        cls.page = CampaignsPage(cls.driver)
        cls.page.open()


class TestGroupListPage(BaseClass):

    # def setup_method(self):
    #     # Refresh page before new test
    #     self.page.refresh()

    def test_open_campaigns_list(self):
        self.page._login_('s.borysenko', 's.borysenko')
        self.page.open_campaigns_tab()

    def test_filter_client_group_by_ucce(self):
        self.page.open_client_group_filter()
        self.page.filter_client_group_by_ucce()
        self.page.open_client_group_filter()

    def test_filter_client_group_by_uccx(self):
        self.page.open_client_group_filter()
        self.page.filter_client_group_by_uccx()
        self.page.open_client_group_filter()

    def test_filter_client_group_by_gmsu(self):
        self.page.open_client_group_filter()
        self.page.filter_client_group_by_gmsu()
        self.page.open_client_group_filter()

    def test_filter_status_by_not_ready(self):
        self.page.open_status_filter()
        self.page.filter_status_by_not_ready()
        self.page.open_status_filter()

    def test_filter_status_by_adding_abonents(self):
        self.page.open_status_filter()
        self.page.filter_status_by_adding_abonents()
        self.page.open_status_filter()

    def test_filter_status_by_ready(self):
        self.page.open_status_filter()
        self.page.filter_status_by_ready()
        self.page.open_status_filter()

    def test_filter_status_by_not_starting(self):
        self.page.open_status_filter()
        self.page.filter_status_by_starting()
        self.page.open_status_filter()

    def test_filter_status_by_in_progress(self):
        self.page.open_status_filter()
        self.page.filter_status_by_in_progress()
        self.page.open_status_filter()

    def test_filter_status_by_getting_result(self):
        self.page.open_status_filter()
        self.page.filter_status_by_getting_result()
        self.page.open_status_filter()


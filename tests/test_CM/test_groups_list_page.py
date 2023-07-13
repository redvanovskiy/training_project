import time

from pages.pages_CM.GroupsListPage import GroupListPage


class BaseClass:

    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        cls.page = GroupListPage(cls.driver)
        cls.page.open()


class TestGroupListPage(BaseClass):

    def setup_method(self):
        # Refresh page before new test
        self.page.refresh()
        self.page._login('s.borysenko', 's.borysenko')

    def test_cyrillic_search(self):
        self.page.set_search_key('тест')

    def test_latin_search(self):
        self.page.set_search_key('test')

    def test_search_by_number(self):
        self.page.set_search_key('7')

    def test_filter_by_ucce(self):
        self.page.open_filter()
        self.page.select_ucce_checkbox()
        self.page.click_ok_button()

    def test_reset_filter(self):
        self.page.cancel_previous_filter()

    def test_filter_by_uccx(self):
        self.page.open_filter()
        self.page.select_uccx_checkbox()
        self.page.click_ok_button()
        time.sleep(1)
        self.page.cancel_previous_filter()

    def test_filter_by_gmsu(self):
        self.page.open_filter()
        self.page.select_gmsu_checkbox()
        self.page.click_ok_button()
        time.sleep(1)
        self.page.cancel_previous_filter()

    def test_filter_by_ucce_and_uccx(self):
        self.page.open_filter()
        self.page.select_ucce_checkbox()
        self.page.select_uccx_checkbox()
        self.page.click_ok_button()
        time.sleep(1)
        self.page.cancel_previous_filter()

    def test_filter_by_uccx_and_gmsu(self):
        self.page.open_filter()
        self.page.select_uccx_checkbox()
        self.page.select_gmsu_checkbox()
        self.page.click_ok_button()
        time.sleep(1)
        self.page.cancel_previous_filter()

    def test_filter_by_ucce_and_gmsu(self):
        self.page.open_filter()
        self.page.select_ucce_checkbox()
        self.page.select_gmsu_checkbox()
        self.page.click_ok_button()
        time.sleep(1)
        self.page.cancel_previous_filter()

    def test_filter_by_ucce_uccx_and_gmsu(self):
        self.page.open_filter()
        self.page.select_ucce_checkbox()
        self.page.select_uccx_checkbox()
        self.page.select_gmsu_checkbox()
        self.page.click_ok_button()
        time.sleep(1)
        self.page.cancel_previous_filter()

    def test_collapse_groups_list(self):
        self.page.click_collapse_button()

    def test_expand_groups_list(self):
        self.page.click_expand_button()

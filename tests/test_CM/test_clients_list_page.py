import time

from pages.pages_CM.ClientsListPage import ClientsListPage


class BaseClass:

    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        cls.page = ClientsListPage(cls.driver)
        cls.page.open()


class TestGroupListPage(BaseClass):

    def setup_method(self):
        # Refresh page before new test
        self.page.refresh()

    def test_open_clients_list(self):
        self.page._login('s.borysenko', 's.borysenko')
        self.page.open_clients_list_tab()

    def test_sort_by_phone(self):
        self.page.sort_by_phone()
        time.sleep(1)
        self.page.sort_by_phone()

    def test_sort_by_clientid(self):
        self.page.sort_by_clientid()
        time.sleep(1)
        self.page.sort_by_clientid()

    def test_sort_by_age(self):
        self.page.sort_by_age()
        time.sleep(1)
        self.page.sort_by_age()

    def test_sort_by_clientname(self):
        self.page.sort_by_clientname()
        time.sleep(1)
        self.page.sort_by_clientname()

    def test_click_refresh_button(self):
        self.page.click_refresh_button()

    def test_download_excel(self):
        self.page.click_export_to_excel_button()

    def test_cansel_changes_displayed_columns(self):
        self.page.check_displayed_columns()
        self.page.select_age_column()
        self.page.select_clientname_column()
        self.page.click_cansel_button()

    def test_change_displayed_columns(self):
        self.page.check_displayed_columns()
        self.page.select_clientid_column()
        self.page.select_phone_column()
        self.page.click_apply_button()

    def test_open_filter(self):
        self.page.open_filter()

    def test_filter_by_batches(self):
        self.page.open_filter()
        self.page.click_add_filter_button()
        self.page.open_field_selector()
        self.page.select_batches()
        self.page.open_batches_name_selector()
        self.page.select_first_batch()
        self.page.click_apply_button()

    def test_filter_by_clientid(self):
        self.page.open_filter()
        self.page.click_add_filter_button()
        self.page.open_field_selector()
        self.page.select_clientid()
        self.page.open_condition_selector()
        self.page.select_match_exactly()
        self.page.set_value('5')
        self.page.confirm_value()
        self.page.click_apply_button()

    def test_filter_by_clientname(self):
        self.page.open_filter()
        self.page.click_add_filter_button()
        self.page.open_field_selector()
        self.page.select_clientmame()
        self.page.open_condition_selector()
        self.page.select_not_match()
        self.page.set_value('Magda')
        self.page.confirm_value()
        self.page.click_apply_button()

    def test_filter_by_phone(self):
        self.page.open_filter()
        self.page.click_add_filter_button()
        self.page.open_field_selector()
        self.page.select_phone()
        self.page.open_condition_selector()
        self.page.select_contain()
        self.page.set_value('9')
        self.page.confirm_value()
        self.page.click_apply_button()

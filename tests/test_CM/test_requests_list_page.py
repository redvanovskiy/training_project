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

    def test_filter_by_clientid_less_0(self):
        self.page.open_filter()
        self.page.click_add_filter_button()
        self.page.open_field_selector()
        self.page.select_clientid()
        self.page.open_condition_selector()
        self.page.select_not_match()
        self.page.set_value('-1')
        self.page.confirm_value()
        self.page.click_apply_button()

    def test_filter_by_clientid_letters(self):
        self.page.open_filter()
        self.page.click_add_filter_button()
        self.page.open_field_selector()
        self.page.select_clientid()
        self.page.open_condition_selector()
        self.page.select_contain()
        self.page.set_value('s')
        self.page.confirm_value()
        self.page.click_apply_button()

    def test_filter_by_clientid_cirilic(self):
        self.page.open_filter()
        self.page.click_add_filter_button()
        self.page.open_field_selector()
        self.page.select_clientid()
        self.page.open_condition_selector()
        self.page.select_start_with()
        self.page.set_value('Ї')
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

    def test_filter_by_clientname_less_0(self):
        self.page.open_filter()
        self.page.click_add_filter_button()
        self.page.open_field_selector()
        self.page.select_clientid()
        self.page.open_condition_selector()
        self.page.select_not_match()
        self.page.set_value('-1')
        self.page.confirm_value()
        self.page.click_apply_button()

    def test_filter_by_clientname_more_0(self):
        self.page.open_filter()
        self.page.click_add_filter_button()
        self.page.open_field_selector()
        self.page.select_clientid()
        self.page.open_condition_selector()
        self.page.select_contain()
        self.page.set_value('7')
        self.page.confirm_value()
        self.page.click_apply_button()

    def test_filter_by_clientname_cirilic(self):
        self.page.open_filter()
        self.page.click_add_filter_button()
        self.page.open_field_selector()
        self.page.select_clientid()
        self.page.open_condition_selector()
        self.page.select_start_with()
        self.page.set_value('Ї')
        self.page.confirm_value()
        self.page.click_apply_button()

    def test_filter_by_clientname_symbols(self):
        self.page.open_filter()
        self.page.click_add_filter_button()
        self.page.open_field_selector()
        self.page.select_clientid()
        self.page.open_condition_selector()
        self.page.select_start_with()
        self.page.set_value('@')
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

    def test_filter_by_requestdatetime_match_exactly(self):
        self.page.open_filter()
        self.page.click_add_filter_button()
        self.page.open_field_selector()
        self.page.select_requestdatetime()
        self.page.open_condition_selector()
        self.page.select_match_exactly()
        self.page.click_now_button()
        self.page.use_only_last_request()
        self.page.click_apply_button()

    def test_filter_by_requestdatetime_not_match(self):
        self.page.open_filter()
        self.page.open_condition_selector()
        self.page.select_not_match()
        self.page.click_apply_button()

    def test_filter_by_requestdatetime_less_than(self):
        self.page.open_filter()
        self.page.open_condition_selector()
        self.page.select_less_than()
        self.page.click_apply_button()

    def test_filter_by_requestdatetime_less_than_or_equal(self):
        self.page.open_filter()
        self.page.open_condition_selector()
        self.page.select_less_than_or_equal()
        self.page.click_apply_button()

    def test_filter_by_requestdatetime_greater_than(self):
        self.page.open_filter()
        self.page.open_condition_selector()
        self.page.select_greater_than()
        self.page.click_apply_button()

    def test_filter_by_requestdatetime_greater_than_or_equal(self):
        self.page.open_filter()
        self.page.open_condition_selector()
        self.page.select_greater_than_or_equal()
        self.page.click_apply_button()

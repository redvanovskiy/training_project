import time

from pages.pages_CM.ReportsListFieldsConstructorPage import ReportsListFieldsConstructorPage


class BaseClass:

    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        cls.page = ReportsListFieldsConstructorPage(cls.driver)
        cls.page.open()


class TestGroupsListFieldsConstructorPage(BaseClass):

    def test_open_fields_constructor(self):
        self.page.login('s.borysenko', 's.borysenko')
        self.page.open_fields_constructor()

    def test_click_add_campaign_button(self):
        self.page.click_create_template_button()

    def test_select_list(self):
        self.page.select_list()

    def test_select_aggregated(self):
        self.page.select_aggregated()

    def test_select_consolidated(self):
        self.page.select_consolidated()

    def test_select_statistic(self):
        self.page.select_statistic()

    def test_click_cancel_button(self):
        self.page.click_cancel_button()

    def test_click_create_button(self):
        self.page.click_create_template_button()
        self.page.select_list()
        self.page.click_create_button()

    def test_set_template_name(self):
        self.page.set_template_name('toster')

    def test_set_random_template_name(self):
        random_template_name = self.page.set_random_template_name(7)
        self.page.set_template_name(random_template_name)

    def test_save_new_template(self):
        self.page.save_new_template()

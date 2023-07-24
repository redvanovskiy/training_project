import time

from pages.pages_CM.CampaignsFieldsConstructorPage import CampaignsFieldsConstructorPage


class BaseClass:

    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        cls.page = CampaignsFieldsConstructorPage(cls.driver)
        cls.page.open()


class TestCampaignsFieldsConstructorPage(BaseClass):

    def test_open_fields_constructor(self):
        self.page.login('s.borysenko', 's.borysenko')
        self.page.open_fields_constructor()

    def test_click_add_campaign_button(self):
        self.page.click_add_campaign_button()

    def test_select_uccx_ucce(self):
        self.page.click_add_campaign_button()
        self.page.click_uccx_ucce_button()

    def test_set_campaign_name(self):
        self.page.set_campaign_name('toster')

    def test_set_random_campaign_name(self):
        random_campaign_name = self.page.set_random_campaign_name(5)
        self.page.set_campaign_name(random_campaign_name)

    def test_set_code(self):
        self.page.set_code('33')

    def test_set_campaign_prefix(self):
        self.page.set_campaign_prefix('69')

    def test_select_inbound_mode(self):
        self.page.open_dialer_mode_selector()
        self.page.select_inbound_mode()

    def test_select_predictiveonly_mode(self):
        self.page.open_dialer_mode_selector()
        self.page.select_predictiveonly_mode()

    def test_select_previewonly_mode(self):
        self.page.open_dialer_mode_selector()
        self.page.select_previewonly_mode()

    def test_select_progressiveonly_mode(self):
        self.page.open_dialer_mode_selector()
        self.page.select_progressiveonly_mode()

    def test_select_previewdirectonly_mode(self):
        self.page.open_dialer_mode_selector()
        self.page.select_previewdirectonly_mode()

    def test_select_abandon(self):
        self.page.open_cisco_campaign_dn_selector()
        self.page.select_abandon()

    def test_select_same_time_next_business_day(self):
        self.page.open_cisco_campaign_dn_selector()
        self.page.select_same_time_next_business_day()

    def test_select_use_campaign_dn(self):
        self.page.open_cisco_campaign_dn_selector()
        self.page.select_use_campaign_dn()

    def test_select_agent_type(self):
        self.page.open_campaign_type_selector()
        self.page.select_agent_type()

    def test_select_ivr(self):
        self.page.open_campaign_type_selector()
        self.page.select_ivr()

    def test_set_comment(self):
        self.page.set_campaign_name('toster')

    def test_set_random_comment(self):
        random_comment = self.page.set_random_comment(7)
        self.page.set_campaign_name(random_comment)

    def test_select_first_time_zone(self):
        self.page.open_time_zone_selector()
        self.page.select_first_time_zone()

    def test_select_first_skill_group(self):
        self.page.open_skill_group_selector()
        self.page.select_first_skill_group()

    def test_click_cancel_button(self):
        self.page.click_cancel_button()

    def test_click_add_button(self):
        self.page.click_add_button()

    def test_create_valid_campaign(self):
        random_campaign_name = self.page.set_random_campaign_name(5)
        random_comment = self.page.set_random_comment(7)
        self.page.click_add_campaign_button()
        self.page.click_uccx_ucce_button()
        self.page.set_campaign_name(random_campaign_name)
        self.page.set_code('11')
        self.page.set_campaign_prefix('77')
        self.page.open_dialer_mode_selector()
        self.page.select_previewonly_mode()
        self.page.open_cisco_campaign_dn_selector()
        self.page.select_same_time_next_business_day()
        self.page.open_campaign_type_selector()
        self.page.select_ivr()
        self.page.set_campaign_name(random_comment)
        self.page.open_time_zone_selector()
        self.page.select_first_time_zone()
        self.page.open_skill_group_selector()
        self.page.select_first_skill_group()
        self.page.click_add_button()




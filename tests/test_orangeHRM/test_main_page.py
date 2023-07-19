from pages.orangeHRM.LoginPage import LoginPage
from pages.orangeHRM.MainPage import MainPage


class BaseClass:

    driver = None
    page = None
    login = None

    @classmethod
    def setup_class(cls):
        cls.login = LoginPage(cls.driver)
        cls.page = MainPage(cls.driver)
        cls.page.open()


class TestSideBar(BaseClass):

    def setup_method(self):
        # Refresh page before new test
        self.page.refresh()

    def test_search_field_is_presented(self):
        self.login._login('Admin', 'admin123')
        self.page.visible(self.page._SEARCH_FIELD)

    def test_admin_button_is_presented_and_clickable(self):
        self.page.visible(self.page._ADMIN_BUTTON)
        self.page.clickable(self.page._ADMIN_BUTTON)

    def test_button_changes_view(self):
        self.page.visible(self.page._ADMIN_BUTTON)
        self.page.click(self.page._ADMIN_BUTTON)
        self.page.visible(self.page._ADMIN_BUTTON_ACTIVE)

    def test_dashboard_button_is_presented_and_clickable(self):
        self.page.visible(self.page._DASHBOARD_BUTTON)
        self.page.clickable(self.page._DASHBOARD_BUTTON)

    def test_search_is_works(self):
        self.page.visible(self.page._DASHBOARD_BUTTON)
        self.page.send_keys(self.page._SEARCH_FIELD, 'adm')
        self.page.visible(self.page._ADMIN_BUTTON)
        self.page.not_visible(self.page._DASHBOARD_BUTTON)
        self.page.not_visible(self.page._DASHBOARD_BUTTON_ACTIVE)

    def test_pim_button_is_presented_and_clickable(self):
        self.page.visible(self.page._PIM_BUTTON)
        self.page.clickable(self.page._PIM_BUTTON)

    def test_leave_button_is_presented_and_clickable(self):
        self.page.visible(self.page._LEAVE_BUTTON)
        self.page.clickable(self.page._LEAVE_BUTTON)

    def test_time_button_is_presented_and_clickable(self):
        self.page.visible(self.page._TIME_BUTTON)
        self.page.clickable(self.page._TIME_BUTTON)

    def test_recruitment_button_is_presented_and_clickable(self):
        self.page.visible(self.page._RECRUITMENT_BUTTON)
        self.page.clickable(self.page._RECRUITMENT_BUTTON)

    def test_my_info_button_is_presented_and_clickable(self):
        self.page.visible(self.page._MY_INFO_BUTTON)
        self.page.clickable(self.page._MY_INFO_BUTTON)

    def test_performance_button_is_presented_and_clickable(self):
        self.page.visible(self.page._PERFORMANCE_BUTTON)
        self.page.clickable(self.page._PERFORMANCE_BUTTON)

    def test_directory_button_is_presented_and_clickable(self):
        self.page.visible(self.page._DIRECTORY_BUTTON)
        self.page.clickable(self.page._DIRECTORY_BUTTON)

    def test_maintenance_button_is_presented_and_clickable(self):
        self.page.visible(self.page._MAINTENANCE_BUTTON)
        self.page.clickable(self.page._MAINTENANCE_BUTTON)

    def test_claim_button_is_presented_and_clickable(self):
        self.page.visible(self.page._CLAIM_BUTTON)
        self.page.clickable(self.page._CLAIM_BUTTON)

    def test_buzz_button_is_presented_and_clickable(self):
        self.page.visible(self.page._BUZZ_BUTTON)
        self.page.clickable(self.page._BUZZ_BUTTON)

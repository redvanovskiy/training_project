import time

from pages.pages_orangehrm import PimPage


class BaseClass:

    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        cls.page = PimPage(cls.driver)
        cls.page.open()


class TestAddEmployee(BaseClass):

    def setup_method(self):
        # Refresh page before new test
        self.page.refresh()

    def test_add_employee(self):
        self.page._login('Admin', 'admin123')
        self.page.open_pim_module()
        self.page._set_credentials()
        time.sleep(2)
        self.page.check_new_profile()
        self.page.click(self.page._EMPLOYEE_LIST)
        time.sleep(2)


class TestDeleteEmployee(BaseClass):

    def setup_method(self):
        # Refresh page before new test
        self.page.refresh()

    def test_delete_employee(self):
        self.page.sort_employee()
        self.page.click_delete_button()
        self.page.click_confirm_button()
        self.page.check_success_message()

from pages.PurchasePath import PurchasePath
from pages.LoginPage import LoginPage




class BaseClass:

    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        cls.page = LoginPage(cls.driver)
        cls.page.open()
        cls.page._login('sm_john_doe', '1234567890')


class TestPurchasePath(BaseClass):



    def setup_method(self):
        # Refresh page before new test
        self.page.refresh()
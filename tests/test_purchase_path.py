from pages.PurchasePath import PurchasePath


class BaseClass:
    
    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        cls.page = PurchasePath(cls.driver)
        cls.page.open()


class TestPurchasePathIncognito(BaseClass):

    fail_msg = 'Please fill out Name and Creditcard.'
    success_msg = 'Product added'
    purchase_msg = 'Thank you for your purchase!'

    def setup_method(self):
        # Refresh page before new test
        self.page.refresh()

    def test_purchase_path_with_empty_set_credential(self):
        self.page.choice_of_goods()
        self.page.set_credential('', '', '', '', '', '')
        self.page.click_purchase_button()
        self.page.assert_text_in_alert(self.fail_msg)
        self.page.accept_alert()
        self.page.click_close_button()
        self.page.back_to_home_page()

    def test_purchase_path(self):
        self.page.choice_of_goods()
        self.page.set_credential('Toster', 'Ukraine', 'Kyiv', 123245456432113456, 6, 2023)
        self.page.confirm_payment_and_check_receipt()


class TestPurchasePathAsUser(BaseClass):

    fail_msg = 'Please fill out all fields.'
    success_msg = 'Product added'
    purchase_msg = 'Thank you for your purchase!'

    def setup_method(self):
        # Refresh page before new test
        self.page.refresh()
        self.page.login('sm_john_doe', '1234567890')
        self.page.visible(self.page._NAME_OF_USER)

    def test_purchase_path_with_empty_set_credential(self):
        self.page.choice_of_goods()
        self.page.set_credential('', '', '', '', '', '')
        self.page.click_purchase_button()
        self.page.assert_text_in_alert(self.fail_msg)
        self.page.accept_alert()
        self.page.click_close_button()
        self.page.back_to_home_page()

    def test_purchase_path(self):
        self.page.choice_of_goods()
        self.page.set_credential('Toster', 'Ukraine', 'Kyiv', 123245456432113456, 6, 2023)
        self.page.confirm_payment_and_check_receipt()


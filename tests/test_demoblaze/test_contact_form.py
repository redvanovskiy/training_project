from pages.pages__demoblaze.ContactFormPage import ContactFormPage


class BaseClass:

    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        cls.page = ContactFormPage(cls.driver)
        cls.page.open()


class ContactForm(BaseClass):

    fail_msg = 'Please fill out all fields.'
    success_msg = 'Thanks for the message!!'
    message_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'

    def setup_method(self):
        # Refresh page before new test
        self.page.refresh()

    def test_failed_sending_message_with_empty_credentials(self):
        self.page.sending_contact_form('', '', '')
        self.page.assert_text_in_alert(self.fail_msg)
        self.page.accept_alert()

    def test_successful_sending(self):
        self.page.sending_contact_form('example@gmail.com', 'toster', self.message_text)
        self.page.assert_text_in_alert(self.success_msg)
        self.page.accept_alert()


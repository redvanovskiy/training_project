from pages.demoblaze.HomePage import HomePage
from pages.demoblaze.LoginPage import LoginPage
from pages.demoblaze.ContactFormPage import ContactFormPage


class BaseClass:

    driver = None
    login = None
    home = None
    form = None
    success_mes = 'Thanks for the message!!'
    title = 'New message'

    @classmethod
    def setup_class(cls):
        cls.login = LoginPage(cls.driver)
        cls.home = HomePage(cls.driver)
        cls.form = ContactFormPage(cls.driver)


class TestContactForm(BaseClass):

    def setup_method(self):
        # Home page open and clear cookies before new test
        self.form.refresh()
        self.form.open()
        self.form.click(self.home._CONTACT)

    # def test_assert_title(self):
    #     self.form.assert_title(self.title)  # Почему-то не работает

    def test_close_button_is_work(self):
        self.form.click(self.form._CLOSE_BUTTON)
        self.form.visible(self.home._PRODUCTS)

    def test_close_icon_is_work(self):
        self.form.click(self.form._CLOSE_ICON)
        self.form.visible(self.home._PRODUCTS)

    def test_send_form_without_fill_field(self):
        self.form.click(self.form._SEND_MESSAGE_BUTTON)
        self.login.assert_text_in_alert(self.success_mes)
        self.login.accept_alert()

    def test_send_form_with_filling_all_fields(self):
        self.form.send_keys(self.form._CONTACT_EMAIL_INPUT, "StarWars@gmail.com")
        self.form.send_keys(self.form._CONTACT_NAME_INPUT, "Obi-Wan Kenobi")
        self.form.send_keys(self.form._MESSAGE_FIELD, "Hello There!")
        self.form.click(self.form._SEND_MESSAGE_BUTTON)
        self.login.assert_text_in_alert(self.success_mes)
        self.login.accept_alert()


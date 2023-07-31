import time

from pages.pages_CM.ClientsListFieldsConstructorPage import ClientsListFieldsConstructorPage


class BaseClass:

    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        cls.page = ClientsListFieldsConstructorPage(cls.driver)
        cls.page.open()


class TestGroupsListFieldsConstructorPage(BaseClass):

    def test_open_fields_constructor(self):
        self.page.login('s.borysenko', 's.borysenko')
        self.page.open_fields_constructor()

    def test_click_add_field_button(self):
        self.page.click_add_field_button()

    def test_set_field_name(self):
        self.page.set_field_name('toster')

    def test_set_random_field_name(self):
        random_field_name = self.page.set_random_field_name(5)
        self.page.set_field_name(random_field_name)

    def test_set_field_title(self):
        self.page.set_field_title('composter')

    def test_set_random_field_title(self):
        random_field_title = self.page.set_random_field_title(7)
        self.page.set_field_name(random_field_title)

    def test_click_save_button(self):
        self.page.click_on_save_button()

    def test_create_valid_new_field(self):
        self.test_click_add_field_button()
        self.test_set_random_field_name()
        self.test_set_random_field_title()
        self.test_click_save_button()

    def test_open_data_type_selector(self):
        self.page.open_data_type_selector()
        self.page.visible(self.page._STRING_TYPE)

    def test_select_string_type(self):
        self.page.open_data_type_selector()
        self.page.select_string_type()

    def test_select_datetime_type(self):
        self.page.open_data_type_selector()
        self.page.select_datetime_type()

    def test_select_date_type(self):
        self.page.open_data_type_selector()
        self.page.select_date_type()

    def test_select_time_type(self):
        self.page.open_data_type_selector()
        self.page.select_time_type()

    def test_select_integer_type(self):
        self.page.open_data_type_selector()
        self.page.select_integer_type()

    def test_select_float_type(self):
        self.page.open_data_type_selector()
        self.page.select_float_type()

    def test_select_text_type(self):
        self.page.open_data_type_selector()
        self.page.select_text_type()

    def test_select_dictionary_type(self):
        self.page.open_data_type_selector()
        self.page.select_dictionary_type()

    def test_click_on_group_checkbox(self):
        self.page.click_on_group_checkbox()

    def test_open_input_type_selector(self):
        self.page.open_input_type_selector()
        self.page.visible(self.page._EDIT_TYPE)

    def test_select_edit_type(self):
        self.page.open_input_type_selector()
        self.page.select_edit_type()

    def test_select_phone_type(self):
        self.page.open_input_type_selector()
        self.page.select_phone_type()

    def test_select_text_type_if_string(self):
        self.page.open_input_type_selector()
        self.page.select_text_type_if_string()

    def test_select_text_type_if_integer(self):
        self.page.open_data_type_selector()
        self.page.select_integer_type()
        self.page.open_input_type_selector()
        self.page.select_text_type_if_integer()

    def test_select_text_type_if_text(self):
        self.page.open_data_type_selector()
        self.page.select_text_type()
        self.page.open_input_type_selector()
        self.page.select_text_type_if_text()

    def test_select_combobox_type(self):
        self.page.open_data_type_selector()
        self.page.select_dictionary_type()
        self.page.open_input_type_selector()
        self.page.select_combobox_type()

    def test_select_radiobuttons_type(self):
        self.page.open_data_type_selector()
        self.page.select_dictionary_type()
        self.page.open_input_type_selector()
        self.page.select_radiobuttons_type()

    def test_select_list_type(self):
        self.page.open_data_type_selector()
        self.page.select_dictionary_type()
        self.page.open_input_type_selector()
        self.page.select_list_type()

    def test_select_buttons_type(self):
        self.page.open_data_type_selector()
        self.page.select_dictionary_type()
        self.page.open_input_type_selector()
        self.page.select_buttons_type()

    def test_open_show_type_selector(self):
        self.page.open_show_type_selector()
        self.page.visible(self.page._MAIN_TYPE)

    def test_select_main_type(self):
        self.page.open_show_type_selector()
        self.page.select_main_type()

    def test_select_second_type(self):
        self.page.open_show_type_selector()
        self.page.select_second_type()

    def test_click_on_is_unique_checkbox(self):
        self.page.click_on_is_unique_checkbox()

    def test_click_on_required_checkbox(self):
        self.page.click_on_required_checkbox()

    def test_click_on_history_checkbox(self):
        self.page.click_on_history_checkbox()

    def test_click_on_filter_checkbox(self):
        self.page.click_on_filter_checkbox()

    def test_set_length(self):
        self.page.open_data_type_selector()
        self.page.select_string_type()
        self.page.set_length('33')

    def test_set_length_256(self):
        self.page.open_data_type_selector()
        self.page.select_string_type()
        self.page.set_length('256')

    def test_set_length_0(self):
        self.page.open_data_type_selector()
        self.page.select_string_type()
        self.page.set_length('0')

    def test_set_length_less_0(self):
        self.page.open_data_type_selector()
        self.page.select_string_type()
        self.page.set_length('-1')

    def test_set_default_value(self):
        self.page.open_data_type_selector()
        self.page.select_string_type()
        self.page.set_default_value('toster')

    def test_click_on_all_symbols_checkbox(self):
        self.page.click_on_all_symbols_checkbox()

    def test_open_dictionary_selector(self):
        self.page.open_dictionary_selector()
        self.page.visible(self.page._FIRST_DICTIONARY)

    def test_select_first_dictionary(self):
        self.page.open_dictionary_selector()
        self.page.select_first_dictionary()

    def test_click_on_delete_last_field_button(self):
        self.page.click_on_delete_last_field_button()

    def test_click_on_cancel_delete_button(self):
        self.page.click_on_delete_last_field_button()
        self.page.click_on_cancel_delete_button()

    def test_click_on_confirm_delete_button(self):
        self.page.click_on_delete_last_field_button()
        self.page.click_on_confirm_delete_button()

    def test_click_on_save_all_button(self):
        self.page.click_on_save_all_button()

    def test_click_on_cancel_all_button(self):
        self.page.click_on_cancel_all_button()

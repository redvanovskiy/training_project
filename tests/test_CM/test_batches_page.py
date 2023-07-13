import time

from pages.pages_CM.BatchesPage import BatchesPage


class BaseClass:

    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        cls.page = BatchesPage(cls.driver)
        cls.page.open()


class TestGroupListPage(BaseClass):
    lorem_ipsum255 = "Lorem ipsum dolor sit amet. Eos nostrum nemo est placeat voluptatem At ipsa quas qui maxime ipsa qui voluptas inventore aut repellendus autem. Et itaque accusantium quo modi officiis est fugit sunt qui quibusdam aperiam in soluta cupiditate. In aspernatur"
    cyrillic_batch_name31 = "Тут якась рандомна назва партії"

    def setup_method(self):
        # Refresh page before new test
        self.page.refresh()
        self.page._login_('s.borysenko', 's.borysenko')

    def test_turn_on_the_switch(self):
        self.page.click_switch_button()
        # self.page.visible(self.page._HIDDEN_ROW)

    def test_turn_off_the_switch(self):
        self.page.click_switch_button()
        # self.page.not_visible(self.page._HIDDEN_ROW)

    def test_select_all_batches(self):
        self.page.select_all_batches()

    def test_select_a_few_batches(self):
        self.page.select_first_batch()
        self.page.select_last_batch()

    def test_hide_batches(self):
        self.page.select_first_batch()
        self.page.select_last_batch()
        self.page.click_hide_batches_button()
        self.page.visible(self.page._SUCCESS_MASSAGE)

    def test_unhide_batches(self):
        self.page.select_all_batches()
        self.page.click_unhide_batches_button()
        self.page.visible(self.page._SUCCESS_MASSAGE)

    def test_create_new_random_batch(self):
        random_batch_name = self.page.set_random_batch_name(7)
        random_batch_comment = self.page.set_random_batch_comment(9)
        self.page.click_create_batch_button()
        self.page.set_batch_name(random_batch_name)
        self.page.set_batch_comment(random_batch_comment)
        self.page.click_add_button()

    def test_delete_batch(self):
        self.page.select_last_batch()
        self.page.click_delete_batches_button()
        self.page.click_confirm_delete()
        self.page.visible(self.page._SUCCESS_MASSAGE)

    def test_create_new_batch_with_empty_comment(self):
        self.page.click_create_batch_button()
        self.page.creating_new_batch('start', '')

    def test_create_new_batch_with_empty_name(self):
        self.page.click_create_batch_button()
        self.page.creating_new_batch('', 'start')

    def test_create_new_batch_with_30_characters_in_name(self):
        random_batch_name = self.page.set_random_batch_name(30)
        self.page.click_create_batch_button()
        self.page.set_batch_name(random_batch_name)
        self.page.click_add_button()

    def test_create_new_batch_with_31_characters_in_name(self):
        random_batch_name = self.page.set_random_batch_name(31)
        self.page.click_create_batch_button()
        self.page.set_batch_name(random_batch_name)
        self.page.click_add_button()
        self.page.visible(self.page._ALERT_MASSAGE)
        self.page.close_alert()

    def test_create_new_batch_with_1_character_in_name(self):
        random_batch_name = self.page.set_random_batch_name(1)
        self.page.click_create_batch_button()
        self.page.set_batch_name(random_batch_name)
        self.page.click_add_button()

    def test_create_new_batch_with_30_cyrillic_characters_in_name(self):
        self.page.click_create_batch_button()
        self.page.set_batch_name('Це тестова назва в 30 символів')
        self.page.click_add_button()

    def test_create_new_batch_with_31_cyrillic_characters_in_name(self):
        self.page.click_create_batch_button()
        self.page.set_batch_name(self.cyrillic_batch_name31)
        self.page.click_add_button()
        self.page.visible(self.page._ALERT_MASSAGE)
        self.page.close_alert()

    def test_create_new_batch_with_1_cyrillic_character_in_name(self):
        self.page.click_create_batch_button()
        self.page.set_batch_name("ї")
        self.page.click_add_button()

    def test_create_new_batch_with_emoji_in_name(self):
        self.page.click_create_batch_button()
        self.page.creating_new_batch('🙃', '')

    def test_create_new_batch_with_255_characters_in_comment(self):
        random_batch_name = self.page.set_random_batch_name(7)
        random_batch_comment = self.page.set_random_batch_comment(255)
        self.page.click_create_batch_button()
        self.page.set_batch_name(random_batch_name)
        self.page.set_batch_comment(random_batch_comment)
        self.page.click_add_button()

    def test_create_new_batch_with_256_characters_in_comment(self):
        random_batch_name = self.page.set_random_batch_name(7)
        random_batch_comment = self.page.set_random_batch_comment(256)
        self.page.click_create_batch_button()
        self.page.set_batch_name(random_batch_name)
        self.page.set_batch_comment(random_batch_comment)
        self.page.click_add_button()
        self.page.visible(self.page._ALERT_MASSAGE)
        self.page.close_alert()

    def test_create_new_batch_with_1_characters_in_comment(self):
        random_batch_name = self.page.set_random_batch_name(7)
        random_batch_comment = self.page.set_random_batch_comment(1)
        self.page.click_create_batch_button()
        self.page.set_batch_name(random_batch_name)
        self.page.set_batch_comment(random_batch_comment)
        self.page.click_add_button()

    def test_create_new_batch_with_1_cyrillic_characters_in_comment(self):
        random_batch_name = self.page.set_random_batch_name(7)
        self.page.click_create_batch_button()
        self.page.set_batch_name(random_batch_name)
        self.page.set_batch_comment("ї")
        self.page.click_add_button()

    def test_create_new_batch_with_emoji_in_comment(self):
        self.page.click_create_batch_button()
        self.page.creating_new_batch('toster', '🙃')

    def test_change_name_last_added_group(self):
        random_batch_name = self.page.set_random_batch_name(7)
        self.page.click_edit_action_button()
        self.page.edit_batch_name(random_batch_name)
        self.page.click_save_changes_button()

    def test_change_comment_last_added_group(self):
        random_batch_comment = self.page.set_random_batch_comment(9)
        self.page.click_edit_action_button()
        self.page.edit_batch_comment(random_batch_comment)
        self.page.click_save_changes_button()

    def test_click_replace_duplicates_checkbox(self):
        self.page.click_add_action_button()
        self.page.click_replace_duplicates_checkbox()

    def test_view_mapping_fields(self):
        self.page.click_add_action_button()
        self.page.view_mapping_fields()
        self.page.visible(self.page._VIEW_MAPPING_FIELDS)
        self.page.close_mapping_fields()

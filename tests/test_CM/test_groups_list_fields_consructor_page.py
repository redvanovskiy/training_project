import time

from pages.pages_CM.GroupsListFieldsConstructorPage import GroupsListFieldsConstructorPage


class BaseClass:

    lorem_ipsum255 = "Lorem ipsum dolor sit amet. Eos nostrum nemo est placeat voluptatem At ipsa quas qui maxime ipsa qui voluptas inventore aut repellendus autem. Et itaque accusantium quo modi officiis est fugit sunt qui quibusdam aperiam in soluta cupiditate. In aspernatur"
    cyrillic_lorem_ipsum255 = "Але я повинен пояснити вам, як народилася вся ця помилкова ідея про засудження задоволення і хвалу болю, і я дам вам повний опис системи та викладу фактичні вчення великого дослідника істини, майстер-будівельник людського щастя. Ніхто не відкидає, не люби"
    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        cls.page = GroupsListFieldsConstructorPage(cls.driver)
        cls.page.open()


class TestGroupsListFieldsConstructorPage(BaseClass):

    def setup_method(self):
        # Refresh page before new test
        self.page.refresh()
        self.page.login('s.borysenko', 's.borysenko')

    def test_open_fields_constructor(self):
        self.page.open_fields_constructor()

    def test_create_new_group_without_campaigns(self):
        self.page.click_add_button()
        self.page.set_group_name('toster')
        self.page.set_comment('composter')
        self.page.click_save_button()

    def test_create_new_group_without_comment_and_campaigns(self):
        self.page.click_add_button()
        self.page.set_group_name('newtoster')
        self.page.click_save_button()

    def test_create_new_group_without_name(self):
        self.page.click_add_button()
        self.page.not_visible(self.page._SAVE_BUTTON)

    def test_create_new_group_with_less_than_30_characters_in_name(self):
        random_group_name = self.page.set_random_group_name(30)
        self.page.click_add_button()
        self.page.set_group_name(random_group_name)
        self.page.click_save_button()

    def test_create_new_group_with_more_than_30_characters_in_name(self):
        random_group_name = self.page.set_random_group_name(31)
        self.page.click_add_button()
        self.page.set_group_name(random_group_name)
        self.page.click_save_button()
        self.page.visible(self.page._ALERT_MASSAGE)
        self.page.close_alert()

    def test_create_new_group_with_1_character_in_name(self):
        random_group_name = self.page.set_random_group_name(1)
        self.page.click_add_button()
        self.page.set_group_name(random_group_name)
        self.page.click_save_button()

    def test_create_new_group_with_1_character_in_comment(self):
        random_group_name = self.page.set_random_group_name(7)
        random_comment = self.page.set_random_comment(1)
        self.page.click_add_button()
        self.page.set_group_name(random_group_name)
        self.page.set_group_name(random_comment)
        self.page.click_save_button()

    def test_create_new_group_with_255_characters_in_comment(self):
        random_group_name = self.page.set_random_group_name(7)
        random_comment = self.page.set_random_comment(255)
        self.page.click_add_button()
        self.page.set_group_name(random_group_name)
        self.page.set_group_name(random_comment)
        self.page.click_save_button()

    def test_create_new_group_with_255_cyrillic_characters_in_comment(self):
        random_group_name = self.page.set_random_group_name(7)
        self.page.click_add_button()
        self.page.set_group_name(random_group_name)
        self.page.set_group_name(self.cyrillic_lorem_ipsum255)
        self.page.click_save_button()

    def test_create_new_group_with_256_characters_in_comment(self):
        random_group_name = self.page.set_random_group_name(7)
        random_comment = self.page.set_random_comment(256)
        self.page.click_add_button()
        self.page.set_group_name(random_group_name)
        self.page.set_group_name(random_comment)
        self.page.click_save_button()

    def test_change_name_last_added_group(self):
        random_group_name = self.page.set_random_group_name(7)
        self.page.open_last_added_group()
        self.page.click_edit_button()
        self.page.edit_group_name(random_group_name)
        self.page.click_save_changes_button()

    def test_change_comment_last_added_group(self):
        random_comment = self.page.set_random_comment(69)
        self.page.open_last_added_group()
        self.page.click_edit_button()
        self.page.edit_comment(random_comment)
        self.page.click_save_changes_button()

    def test_add_gmsu_to_the_previously_created_ucce_group(self):
        random_group_name = self.page.set_random_group_name(30)
        self.page.click_add_button()
        self.page.set_group_name(random_group_name)
        self.page.click_use_in_campaigns_button()
        self.page.click_ucce_radiobutton()
        self.page.click_save_button()
        self.page.open_last_added_group()
        self.page.click_edit_button()
        self.page.click_use_in_campaigns_edit_button()
        self.page.select_gmsu_checkbox()

    def test_add_gmsu_to_the_previously_created_uccx_roup(self):
        random_group_name = self.page.set_random_group_name(30)
        self.page.click_add_button()
        self.page.set_group_name(random_group_name)
        self.page.click_use_in_campaigns_button()
        self.page.click_uccx_radiobutton()
        self.page.click_save_button()
        self.page.open_last_added_group()
        self.page.click_edit_button()
        self.page.click_use_in_campaigns_edit_button()
        self.page.select_gmsu_checkbox()

    def test_delete_comment_last_added_group(self):
        self.page.open_last_added_group()
        self.page.click_edit_button()
        self.page.edit_comment('')
        self.page.click_save_changes_button()

    def test_delete_name_last_added_group(self):
        self.page.open_last_added_group()
        self.page.click_edit_button()
        self.page.edit_group_name('')
        self.page.not_visible(self.page._SAVE_BUTTON)
        self.page.click_save_changes_button()

    def test_delete_last_added_group(self):
        self.page.open_last_added_group()
        self.page.click_edit_button()
        self.page.click_delete_button()
        self.page.confirm_delete_button()
        self.page.visible(self.page._SUCCESS_MASSAGE)
        self.page.close_alert()










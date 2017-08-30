from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # User accesses the page and tries to submit empty list item
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        # The page refreshes and there ia and error message saying
        # that list items cannot be blank

        self.browser.find_elements_by_css_selector('#id_text:valid')
        # error = self.browser.find_element_by_css_selector('.has-error')
        # self.assertEqual(error.text, "You can't have an empty list item")

        # User tries again with some text in the text box and it works
        self.get_item_input_box().send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')

        # User again decides to send empty item
        self.get_item_input_box().send_keys('\n')

        # and gets an error message again
        self.check_for_row_in_list_table('1: Buy milk')
        self.browser.find_elements_by_css_selector('#id_text:valid')
        # error = self.browser.find_element_by_css_selector('.has-error')
        # self.assertEqual(error.text, "You can't have an empty list item")

        # then user corrects it by filling with some text
        self.get_item_input_box().send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')

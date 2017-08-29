from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_and_retrieve_it_later(self):

        # There's a brand new online TO DO app which can be accessed via
        self.browser.get(self.server_url)

        # Page title and header mention to do list
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('to-do', header_text)

        # One can add items straightaway
        input_box = self.get_item_input_box()
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter an item'
        )

        # One types 'Learn python' into a text box
        input_box.send_keys('Learn Python')

        # When one hits enter, new page is open and now the page lists
        # '1: Learn Python' as an item on the list
        input_box.send_keys(Keys.ENTER)
        user_list_url = self.browser.current_url
        self.assertRegex(user_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Learn Python')

        # There is still a text box to enter another item
        # One enters 'Use Python to make a web app'
        input_box = self.get_item_input_box()
        input_box.send_keys('Use Python to make a web app')
        input_box.send_keys(Keys.ENTER)

        # The page updates again and there're two items now
        self.check_for_row_in_list_table('1: Learn Python')
        self.check_for_row_in_list_table('2: Use Python to make a web app')

        # Another user opens the site
        # New browser session to make sure that no information of previous user is coming through
        self.browser.quit()
        self.browser = webdriver.Chrome()

        # New user visits the page and there is no data form previous user
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Learn Python', page_text)
        self.assertNotIn('Use Python to make a web app', page_text)

        # New user starts a new list by entering a new item
        input_box = self.get_item_input_box()
        input_box.send_keys('Buy milk')
        input_box.send_keys(Keys.ENTER)

        # New user gets its onw unique URL
        new_user_list_url = self.browser.current_url
        self.assertRegex(new_user_list_url, '/lists/.+')
        self.assertNotEqual(new_user_list_url, user_list_url)

        # Double check for previous user data
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Learn Python', page_text)
        self.assertIn('Buy milk', page_text)

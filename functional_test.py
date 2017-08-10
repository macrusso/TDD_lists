from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_general(self):

        # There's a brand new online TO DO app which can be accessed via
        self.browser.get('http://127.0.0.1:8000/')

        # Page title and header mention to do list
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # One can add items straightaway
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # One types 'Learn python' into a text box
        input_box.send_keys('Learn Python')

        # When one hits enter, the page updates and now the page lists
        # '1: Learn Python' as an item on the list
        input_box.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1: Learn Python')

        # There is still a text box to enter another item
        # One enters 'Use Python to make a web app'
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('Use Python to make a web app')
        input_box.send_keys(Keys.ENTER)

        # The page updates again and there're two items now
        self.check_for_row_in_list_table('1: Learn Python')
        self.check_for_row_in_list_table('2: Use Python to make a web app')

        # To remember the list, the page generates an unique URL for an user
        self.fail('Finish the test!')
        # Once revisited that URL, one realises its list is still there

        # One closes the window

if __name__ == '__main__':
    unittest.main(warnings='ignore')



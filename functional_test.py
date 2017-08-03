from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_general(self):

        # There's a brand new online TO DO app which can be accessed via
        self.browser.get('http://127.0.0.1:8000/')

        # Page title and header mention to do list
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # One can add items straightaway

        # One types 'Learn python' into a text box

        # When one hits enter, the page updates and now the page lists
        # '1: Learn python' as an item on the list

        # There is still a text box to enter another item
        # One enters 'Use python to make a web app'

        # The page updates again and there're two items now

        # To remember the list, the page generates an unique URL for an user

        # Once revisited that URL, one realises its list is still there

        # One closes the window

if __name__ == '__main__':
    unittest.main(warnings='ignore')



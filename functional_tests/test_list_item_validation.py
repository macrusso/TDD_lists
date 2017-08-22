from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # User accesses the page and tries to submit empty list item

        # The page refreshes and there ia and error message saying
        # that list items cannot be blank

        # User tries again with some text in the text box and it works

        # User again decides to send empty item

        # and gets an error message again

        # end
        self.fail('write me!')

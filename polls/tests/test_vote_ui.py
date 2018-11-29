from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest

class VoteUITest(unittest.TestCase):
    # class variable can be accessed via class name or 'self'
    BASE_URL = 'http://localhost:8000'

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def no_test_get_polls_index(self):
        self.browser.get(self.BASE_URL + '/polls/')
        # Page title should include string "Polls"
        self.assertIn('Polls', self.browser.title)
        # The page also contains a header mentioning "programming"
        header_text = self.browser.find_element_by_tag_name('h1')
        self.assertIn("Programming", header_text)
        

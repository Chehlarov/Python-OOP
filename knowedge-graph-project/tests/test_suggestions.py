import unittest
from suggstions import Suggestions

class SuggestionTest(unittest.TestCase):
    def test_parse_of_content(self):
        content = 'miki'
        Suggestions.get_element_tree(content)



if __name__ == '__main__':
    unittest.main()
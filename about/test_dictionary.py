import unittest

class DictionaryTestCase(unittest.TestCase):
    def setUp(self):
        """ This is run before every test """
        self.colors = {"red"   : 0xff0000,
                       "green" : 0x00ff00,
                       "blue"  : 0x0000ff
        }

    def test_dictionary_definition(self):
        """ Dictionary syntax does not rely on whitespace.
        It uses braces, colons for key : value and commas between entries. """

        colors_2 = { "red" : 0xFF0000, "green" : 0x00FF00, "blue" : 0x0000FF }
        self.assertDictEqual(self.colors, colors_2, "The dictionaries should contain identical entries")

    def test_dictionary_in(self):
        """ Keyword `in` is used to test if a dict contains a certain key """
        self.assertTrue("red" in self.colors, "The dictionary should contain the entry 'red'")
        self.assertFalse("rot" in self.colors, "'in' should return false for unknown keys")

if __name__ == "__main__":
    unittest.main()

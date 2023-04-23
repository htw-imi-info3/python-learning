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

    def test_dictionary_get(self):
        """ the get method returns the value to a key or None if the key does not exist """
        self.assertEqual(self.colors.get("red"), 0xff0000)
        self.assertIsNone(self.colors.get("rot"))

    def test_dictionary_list_access(self):
        """ dictionary entries can also be accessed like lists with the key in square brackets """
        self.assertEqual(self.colors["red"], 0xff0000)

        # Trying to access a non existent key should raise a KeyError
        with self.assertRaises(KeyError):
            print(self.colors["rot"])

    def test_empty_dictionary_is_false(self):
            empty_dict = {}
            self.assertFalse(empty_dict)

if __name__ == "__main__":
    unittest.main()

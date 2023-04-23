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

    def test_dictionary_definition_alternative(self):
        """ If the keys follow variable naming conventions (no whitespace, no leading numbers ...) then
        Dictionaries can be defined using the dict constructor. The keys are stored as strings. """
        colors_2 = dict(red=0xff0000, green=0x00ff00, blue=0x0000ff)
        self.assertDictEqual(self.colors, colors_2, "The dictionaries should contain identical entries")

        for key in colors_2.keys():
            self.assertEqual(type(key), str, "All keys should be strings right now")

    def test_dictionary_in(self):
        """ Keyword `in` is used to test if a dict contains a certain key """
        self.assertTrue("red" in self.colors, "The dictionary should contain the entry 'red'")
        self.assertFalse("rot" in self.colors, "'in' should return false for unknown keys")

    def test_dictionary_get(self):
        """ the get method returns the value to a key or None if the key does not exist """
        self.assertEqual(self.colors.get("red"), 0xff0000)
        self.assertIsNone(self.colors.get("rot"))

    def test_dictionary_get_default(self):
        """ the get method accepts an optional parameter for a default value that is
        returned when the key is not in the dict """
        self.assertNotIn("rot", self.colors, "The key should not be in the dict")
        red = self.colors.get("rot", 0xff0000)
        self.assertEqual(red, 0xff0000, "The default value is returned instead of None")

    def test_dictionary_get_setdefault(self):
        """ setdefault works like get(key[, optional_value]),
        but it also adds the key with the default value if its missing """
        self.assertNotIn("white", self.colors, "The key white should not be in the dict yet")

        red = self.colors.setdefault("red", 0xffffff)
        white = self.colors.setdefault("white", 0xffffff)

        self.assertIn("white", self.colors, "The key white should be in the dict now")
        self.assertEqual(red, 0xff0000)
        self.assertEqual(white, 0xffffff)

    def test_dictionary_list_access(self):
        """ dictionary entries can also be accessed like lists with the key in square brackets """
        self.assertEqual(self.colors["red"], 0xff0000)

        # Trying to access a non existent key should raise a KeyError
        with self.assertRaises(KeyError):
            print(self.colors["rot"])

    def test_empty_dictionary_is_false(self):
        empty_dict = {}
        self.assertFalse(empty_dict)

    def test_add(self):
        """ Adding or overwriting a dict entry is a simple assignment """
        self.assertNotIn("white", self.colors, "The key white should not be in the dict yet")
        self.colors["white"] = 0xffffff
        self.assertIn("white", self.colors, "The key white should be in the dict now")

    def test_add_plusequals_undefined(self):
        """ This is not a valid way to add entries """
        with self.assertRaises(TypeError):
            self.colors += {"white" : 0x000000}

    def test_zip(self):
        """ A zip object is used to assemble a dictionary from two iterable types like lists, strings or tuples.
        If they have a different length, zip will stop once one iterable is consumed."""
        keys = ["red", "green", "blue"]
        values = [0xff0000, 0x00ff00, 0x0000ff]
        colors_2 = dict(zip(keys, values))
        self.assertDictEqual(self.colors, colors_2, "These dictionaries should contain equal entries, maybe the fixture was changed?")

    def test_update(self):
        """ Update is used to join two dictionaries, overwriting already present keys """
        colors_2 = {"white" : 0xffffff, "red" : 0}
        colors_2.update(self.colors)
        self.assertIn("green", colors_2, "The green key should be added from the test fixture")
        self.assertEqual(colors_2["red"], 0xff0000, "The value of red should be updated from the test fixture")

    def test_copy(self):
        # TODO: implement
        self.assertTrue(False)

    def test_empty_key(self):
        # TODO: implement
        self.assertTrue(False)

    def test_multiple_key_types(self):
        # TODO: implement
        self.assertTrue(False)

    def test_multiple_value_types(self):
        # TODO: implement
        self.assertTrue(False)

    def test_dict_to_list(self):
        """ The keys, values and items functions return different views on the dictionarys.
        They return their own iterable types, similar to list, but an explicit cast to list
        is necessary when one is needed """

        keys = self.colors.keys()
        values = self.colors.values()
        items = self.colors.items()
        self.assertNotEqual(type(keys), list)
        keys_list = list(keys)
        self.assertEqual(type(keys_list), list)

        colors_2 = dict(zip(keys, values))
        colors_3 = dict(items)
        self.assertDictEqual(self.colors, colors_2)
        self.assertDictEqual(self.colors, colors_3)

    def test_clear(self):
        # TODO: implement
        self.assertTrue(False)

if __name__ == "__main__":
    unittest.main()

import unittest

class DictionaryTestCase(unittest.TestCase):
    def test_dictionary_definition(self):

        colors = {"red"   : 0xff0000,
                  "green" : 0x00ff00,
                  "blue"  : 0x0000ff
        }
        
        colors_2 = { "red" : 0xFF0000, "green" : 0x00FF00, "blue" : 0x0000FF }

        self.assertDictEqual(colors, colors_2, "The dictionaries should contain identical entries")

if __name__ == "__main__":
    unittest.main()

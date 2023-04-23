import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.str1 = 'Hello'
        self.str2 = 'Python'
        self.year = 2023

    def test_upper(self):
        self.assertEqual(self.str1.upper(), 'HELLO')

    def test_isupper(self):
        self.assertFalse(self.str1.isupper())
        self.assertTrue(self.str1.upper().isupper())

    def test_split(self):
        s = self.str2 + ' ' + self.str1
        self.assertEqual(s.split(), ['Python', 'Hello'])
        with self.assertRaises(TypeError):
            s.split(2)

    def test_format(self):
        s = self.str1 + " " + self.str2 + " {}"
        self.assertEqual(s.format(self.year), "Hello Python 2023")

    def test_replace(self):
        s = "Hi, this is the test for Java. You can learn everything from Java here."
        self.assertEqual(s.replace('Java', 'Python'),
                         "Hi, this is the test for Python. You can learn everything from Python here.")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

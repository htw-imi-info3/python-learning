import unittest


class TypingTestCase(unittest.TestCase):
    def test_strong_typing(self):
        with self.assertRaises(TypeError):
            actual = "blabla" + 3
        

if __name__ == '__main__':
    unittest.main()

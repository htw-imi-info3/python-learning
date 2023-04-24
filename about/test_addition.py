import unittest


class TestAddition(unittest.TestCase):
    
    def test_addition(self):
        number = 1 + 2
        self.assertEqual(3, number)


if __name__ == '__main__':
    unittest.main()

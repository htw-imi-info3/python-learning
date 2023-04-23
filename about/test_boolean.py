import unittest

import a as a

from main import boolean, basic_potatos, hello


class MyTestCase(unittest.TestCase):
    def test_even_number(self):
        result = boolean(2)
        expected = "2 is even."
        self.assertEqual(result, expected)

    def test_odd_number(self):
        result = boolean(3)
        expected = "3 is odd."
        self.assertEqual(result, expected)

    def test_size_A(self):
        self.assertEqual(basic_potatos(2.6), "A")

    def test_size_B(self):
        self.assertEqual(basic_potatos(1.75), "B")

    def test_size_C(self):
        self.assertEqual(basic_potatos(1.0), "C")

    def test_size_UNKNOWN(self):
        self.assertEqual(basic_potatos(3.0), "A")

    def test_hello(self):
        result = hello()
        expected = False
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()


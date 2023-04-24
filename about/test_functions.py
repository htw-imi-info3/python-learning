import unittest


class Testfunctions(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(functions.is_prime(4))
        self.assertTrue(functions.is_prime(2))
        self.assertTrue(functions.is_prime(3))
        self.assertFalse(functions.is_prime(8))
        self.assertFalse(functions.is_prime(10))
        self.assertTrue(functions.is_prime(7))
        self.assertEqual(functions.is_prime(-3),
                         "Negative numbers are not allowed")


if __name__ == '__main__':
    unittest.main()
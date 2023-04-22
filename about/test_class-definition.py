import unittest
import inspect


class ClassDefinitionTestCase(unittest.TestCase):

    def setUp(self):
        self.test_cases = {
            int: True,
            float: True,
            complex: True,
            True: False,
            False: False,
            None: False
        }

    def test_isclass(self):
        for key in self.test_cases:
            self.assertEqual(inspect.isclass(key), self.test_cases[key])


if __name__ == '__main__':
    unittest.main()

import unittest
import inspect


class ClassDefinitionTestCase(unittest.TestCase):

    class_types = [int, float, complex]
    other_types = [True, False, None]

    @classmethod
    def setUpClass(cls):
        cls.test_cases = dict.fromkeys(cls.class_types, True) | dict.fromkeys(cls.other_types, False)
        if len(cls.test_cases) != len(cls.class_types) + len(cls.other_types):
            raise ValueError("test_cases and the sum of class_types and other_types differ in length.")

    def test_isclass(self):
        for key in self.test_cases:
            self.assertEqual(inspect.isclass(key), self.test_cases[key])


if __name__ == '__main__':
    unittest.main()

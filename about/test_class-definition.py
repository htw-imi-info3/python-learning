import unittest
import inspect


class ClassDefinitionTestCase(unittest.TestCase):

    def setUp(self):
        self.test_cases = {
            'py_class_list': [
                int,
                float,
                complex
            ],
            'py_non_class_list': [
                True,
                False,
                None
            ]
        }
        self.example_variable = int

    def test_isclass(self):
        for built_in_class in self.test_cases['py_class_list']:
            self.assertTrue(inspect.isclass(built_in_class))
        for built_in_class in self.test_cases['py_non_class_list']:
            self.assertFalse(inspect.isclass(built_in_class))
        self.assertTrue(inspect.isclass(self.example_variable),
                        msg='"' + str(self.example_variable) + '" is not a class.')


if __name__ == '__main__':
    unittest.main()

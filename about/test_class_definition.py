import unittest
import inspect


class ClassDefinitionTestCase(unittest.TestCase):
    # inspect.isclass() should return True:
    class_types = [int, float, complex]
    # inspect.isclass() should return False:
    other_types = [True, False, None]

    @classmethod
    def setUpClass(cls):
        cls.test_cases = dict.fromkeys(cls.class_types, True) | dict.fromkeys(cls.other_types, False)
        if len(cls.test_cases) != len(cls.class_types) + len(cls.other_types):
            raise ValueError('"class_types" and "other_types" must not have any common items.')

    def test_inspect_isclass(self):
        """use self.test_cases to test inspect.isclass()"""
        for key in self.test_cases:
            with self.subTest(key=key):
                self.assertEqual(inspect.isclass(key),
                                 self.test_cases[key],
                                 msg='"' + str(key) + '" is ' + ('' if self.test_cases[key] else 'not ')
                                     + 'a class and should return ' + str(self.test_cases[key])
                                     + ', but returns ' + str(not self.test_cases[key]))


if __name__ == '__main__':
    unittest.main()

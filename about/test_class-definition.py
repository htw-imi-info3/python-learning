import unittest
import inspect



class ClassDefinitionTestCase(unittest.TestCase):

    def test_isclass(self):
        self.assertTrue(inspect.isclass())


if __name__ == '__main__':
    unittest.main()

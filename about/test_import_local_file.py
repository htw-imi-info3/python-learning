import unittest
import test_import


class TestLocalModule(unittest.TestCase):

    def test_import_local_file(self):
        self.assertIsNotNone(test_import)

    def test_greet_function(self):
        names = ["Name1", "Name2", "Name3", "Name4"]
        for name in names:
            greeting = test_import.greet(name)
            self.assertEqual(greeting, "Hello, " + name + "!")
            print(greeting)


if __name__ == '__main__':
    unittest.main()

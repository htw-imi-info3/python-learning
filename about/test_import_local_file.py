import unittest
import testimport
import random


class TestImportLocalFile(unittest.TestCase):
    names = ['Mathieu', 'Imanuel', 'Timo', 'Sascha', 'Chris', 'Jesus']

    def test_import_local_file(self):
        print("Running test_import_local_file...")
        name = random.choice(self.names)
        greeting = testimport.greet(name)
        print(greeting)
        self.assertEqual(greeting, "Hello, " + name + "!")


if __name__ == '__main__':
    unittest.main()

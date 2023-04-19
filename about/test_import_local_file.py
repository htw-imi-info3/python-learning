import unittest
import testimport


class TestImportLocalFile(unittest.TestCase):

    def test_import_local_file(self):
        name = "Mathieu"
        greeting = testimport.greet(name)
        self.assertEqual(greeting, "Hello, Mathieu!")


if __name__ == '__main__':
    unittest.main()

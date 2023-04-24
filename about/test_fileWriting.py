import unittest
import os


class MyTestCase(unittest.TestCase):
    def test_fileWriter(self):
        # creating a temporary file and writing in it
        with open('testFile.txt', 'w') as temp_file:
            temp_file.write("this is a test")

        # looking if the written text is correct
        with open(temp_file.name, 'r') as file:
            self.assertEqual(file.read(), "this is a test")

        # deleting the temporary file
        os.remove(temp_file.name)


if __name__ == '__main__':
    unittest.main()

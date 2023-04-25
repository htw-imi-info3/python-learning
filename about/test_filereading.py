import unittest


class TestFile(unittest.TestCase):
    def test_filereading(self):
        expected_output = "AusgabeAusgabe"
        try:
            with open("lab2reading.txt", "r") as f:
                content = f.read().strip()
            if content == expected_output:
                print("Test passed: Content matches the output.")
            else:
                print("Test failed: Content doesn't match the output.")
                self.fail()
        except FileNotFoundError:
            print("Test failed: File not found.")
            self.fail()


if __name__ == '__main__':
    unittest.main()

import unittest


class TestConditional(unittest.TestCase):
    def test_if(self):
        result = "none"
        a = 6
        if a == 5:
            result = 5
        else:
            result = "not 5"

        self.assertEqual("not 5", result, "the else case should be used")


if __name__ == '__main__':
    unittest.main()

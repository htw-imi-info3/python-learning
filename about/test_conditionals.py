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


    def dangling_else_1(self, a):
        if a == 1:
            return 1
            if a == 2:
                return 2
            else:
                return 3

    def dangling_else_2(self, a):
        if a == 1:
            result = 1
            if a == 2:
                result = 2
        else:
            result = 3
        return result


if __name__ == '__main__':
    unittest.main()

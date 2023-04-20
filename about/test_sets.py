import unittest


class WindowTest(unittest.TestCase):
    set1 = {"Bread", "Apple", "Banana"}
    set2 = {"Bread", "Apple", "Apple"}
    set3 = {"Cucumber", "Avocado", "Water"}
    set4 = {}
    set5 = set(set4)

    def SetUp(self):
        self.set1 = {"Bread", "Apple", "Banana"}
        self.set2 = {"Bread", "Apple"}
        self.set3 = {"Cucumber", "Avocado", "Water"}
        self.set4 = {}
        self.set5 = set(self.set4)

    # tests with the empty set
    def test_empty_set_type(self):
        # what type is an empty set?
        self.assertEqual(type(self.set4), dict)

    def test_empty_set1(self):
        self.assertIsNotNone(self.set4)

    def test_empty_set2(self):
        self.assertEqual(len(self.set4), 0)

    # tests dealing with .union() command
    def test_union_set1_set4(self):
        result = self.set1.union(self.set4)
        self.assertEqual(result, self.set1)


if __name__ == '__main__':
    unittest.main()

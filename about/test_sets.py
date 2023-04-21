import unittest


class WindowTest(unittest.TestCase):
    set1 = {"Bread", "Apple", "Banana"}
    set2 = {"Bread", "Apple"}
    set3 = {"Cucumber", "Avocado", "Water"}
    set4 = {}
    set5 = set(set4)

    def setUp(self):
        self.set1 = {"Bread", "Apple", "Banana"}
        self.set2 = {"Bread", "Apple"}
        self.set3 = {"Cucumber", "Avocado", "Water"}
        self.set4 = {}
        self.set5 = set(self.set4)

    def tearDown(self):
        self.set1 = {}
        self.set2 = {}
        self.set3 = {}
        self.set4 = {}
        self.set5 = {}

    # tests with the empty set
    def test_empty_set_type(self):
        # what type is an empty set? ->declared as dict!
        self.assertEqual(type(self.set4), dict)

    def test_empty_set1(self):
        self.assertIsNotNone(self.set4)

    def test_empty_set2(self):
        self.assertEqual(len(self.set4), 0)

    # tests dealing with .union() command
    # union will contain all elements from both sides without duplicates
    def test_union_set1_set4(self):
        result = self.set1.union(self.set4)
        self.assertEqual(result, self.set1)

    # duplicate values will only be kept once
    def test_union_set1_set2(self):
        result = self.set1.union(self.set2)
        self.assertEqual(result, self.set1)

    # intersection will only keep the values which occur in BOTH sets:
    def test_intersect_set1_set2(self):
        result = self.set1.intersection(self.set2)
        self.assertEqual(result, self.set3)

    # the difference between two sets is the set of all the
    # elements in first set that are not present in the second set
    def test_intersect_set1_set2(self):
        result = str(self.set1.difference(self.set2))
        banana = {"Banana"}
        message = f"1 {result} 2 {type(result)} 3 {str(result)}"
        self.assertTrue(str(result)=="{'Banana'}", message)





if __name__ == '__main__':
    unittest.main()

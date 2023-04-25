import unittest

class TestArrayMethods(unittest.TestCase):

    def test_access_element(self):
        my_array = [1, 2, 3, 4, 5]
        self.assertEqual(my_array[2], 3)

    def test_change_element(self):
        my_array = [1, 2, 3, 4, 5]
        my_array[1] = 10
        self.assertEqual(my_array[1], 10)

    def test_iterate_array(self):
        my_array = [1, 2, 3, 4, 5]
        result = []
        for element in my_array:
            result.append(element)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_array_length(self):
        my_array = [1, 2, 3, 4, 5]
        self.assertEqual(len(my_array), 5)

    def test_add_element(self):
        my_array = [1, 2, 3, 4, 5]
        my_array.append(6)
        self.assertEqual(my_array, [1, 2, 3, 4, 5, 6])

    def test_remove_element(self):
        my_array = [1, 2, 3, 4, 5]
        my_array.remove(4)
        self.assertEqual(my_array, [1, 2, 3, 5])

if name == 'main':
    unittest.main()
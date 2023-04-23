import unittest

class TestForLoop(unittest.TestCase):

    def test_1(self):
        list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        list2 = []
        for x in range(10):
            list2.append(x)
        self.assertEqual(list1,list2)

    def test_2(self):
        list1 = []
        list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for x in range(10):
            list2.pop()
        self.assertEqual(list1,list2)

    #Vorschlag 
    def test_3(self):
        list1 = []
        for x in range (0,10):
            list1.append(x)
        self.assertEqual(list1, list(range(0, 10)))

if __name__ == '__main__':
    unittest.main()

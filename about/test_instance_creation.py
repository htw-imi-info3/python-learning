import unittest


class Movie:

    def __init__(self, name, length):
        self.name = name
        self.length = length

    def getLength(self):
        return self.length


class Book:

    def __init__(self, name, pages):
        self.name = name
        self.pages = pages

    def getPages(self):
        return self.pages


class TestClass(unittest.TestCase):

    """def setUp(self):
        self.movie1 = Movie('Perks of Being a Wallflower', 142)
        self.book1 = Book('Diary of an Oxygen Thief', 224)"""

    # test function to test whether obj is instance of class
    def test_negative(self):
        movie2 = Movie('Carol', 159)
        # error message in case if test case got failed
        message = "given object is not instance of Book."
        # assertIsInstance() to check if obj is instance of class
        self.assertNotIsInstance(movie2, Book, message)

    # test function to test whether obj is instance of class
    def test_positive(self):
        movie2 = Movie('Carol', 159)
        # error message in case if test case got failed
        message = "given object is not instance of Movie."
        # assertIsInstance() to check if obj is instance of class
        self.assertIsInstance(movie2, Movie, message)

    def test_getPages(self):
        # creating obj of class
        book1 = Book('Diary of an Oxygen Thief', 224)
        # test if method equals expected output with assertEqual()
        self.assertEqual(book1.getPages(), 224)

    def test_getLength(self):
        # creating obj of class
        movie1 = Movie('Perks of Being a Wallflower', 142)
        # test if method equals expected output with assertEqual()
        self.assertEqual(movie1.getLength(), 142)


if __name__ == '__main__':
    unittest.main()

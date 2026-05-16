import unittest
import sys
import os

# Yeh 2 lines isliye hain taa ke 'tests' folder 'src' folder ki file ko access kar sake
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import library_system

class TestLibrarySystem(unittest.TestCase):

    def setUp(self):
        # Har naye test run hone se pehle dictionary ko clear karna taa ke fresh testing ho
        library_system.library_books.clear()

    # TC-01: Add a new book successfully
    def test_add_new_book(self):
        success, msg = library_system.add_book("101", "Python Basics")
        self.assertTrue(success)
        self.assertEqual(msg, "Book 'Python Basics' added successfully.")
        self.assertIn("101", library_system.library_books)

    # TC-02: Add a book with an existing ID
    def test_add_existing_book(self):
        library_system.add_book("101", "Python Basics")
        success, msg = library_system.add_book("101", "C++")
        self.assertFalse(success)
        self.assertEqual(msg, "Book ID already exists.")

    # TC-03: Borrow an available book
    def test_borrow_available_book(self):
        library_system.add_book("102", "Data Science")
        success, msg = library_system.borrow_book("102")
        self.assertTrue(success)
        # Check that the book's status is now False (Borrowed)
        self.assertFalse(library_system.library_books["102"]["available"])

    # TC-04: Borrow a book that is already borrowed
    def test_borrow_unavailable_book(self):
        library_system.add_book("103", "Machine Learning")
        library_system.borrow_book("103") # First borrow
        success, msg = library_system.borrow_book("103") # Try to borrow again
        self.assertFalse(success)
        self.assertEqual(msg, "Book is already borrowed.")

    # TC-05: Return a borrowed book
    def test_return_book(self):
        library_system.add_book("104", "AI Fundamentals")
        library_system.borrow_book("104") # Borrow it first
        success, msg = library_system.return_book("104") # Now return it
        self.assertTrue(success)
        # Check that the book's status is back to True (Available)
        self.assertTrue(library_system.library_books["104"]["available"])

if __name__ == '__main__':
    unittest.main()
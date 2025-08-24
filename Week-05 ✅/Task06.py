# Week-05/Task06.py
# Task 6: Create a program to manage a library system using
# classes, including methods for adding, removing, and displaying
# books.
print ("=== TASK #6 OUTPUT ===")

class Library:
    def __init__(self):
        self.books = []
    
    print("Added books: ")
    def add_book(self, book):
        self.books.append(book)
        print(book)
    
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Removed books: ", book)
        else: 
            print("Book not Found!")

    def display_book(self):
        print("Books currently in the Library: ")
        for book in self.books:
            print(book)

lib = Library()
lib.add_book("Python")
lib.add_book("Java")
lib.add_book("C++")
lib.add_book("CSS")
lib.remove_book("Python")
lib.display_book()


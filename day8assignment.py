class LibraryBook:
    def __init__(self, title, author, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"{self.title} has been borrowed.")
        else:
            print("This book is already borrowed.")

    def return_book(self):
        self.available = True
        print(f"{self.title} has been returned.")

    def details(self):
        print(f"Title : {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN  : {self.isbn}") 
        print(f"Year   : {self.year}") 


#creating three book objects
book1 = LibraryBook("Python Basics", "John smith", "9781234567890") 
book2 = LibraryBook("clean code", "robert martin", "9780132350884") 
book3 = LibraryBook("Atomic Habits", "James clear", "9780735211292") 

books = [book1, book2, book3]

for book in books:
    book.details()
    book.borrow()
    book.return_book()
    print()  # blank line for spacing


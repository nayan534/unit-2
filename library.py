class Library:
    def __init__(self, books):
        self.books = books

    def show_books(self):
        print(self.books)

    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Borrowed:", book)
        else:
            print("Not Available")

    def return_book(self, book):
        self.books.append(book)

lib = Library(["Python", "Java", "C++"])
lib.show_books()
lib.borrow_book("Python")
lib.return_book("Python")

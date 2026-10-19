class Book:
    total_books = 0  

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

        Book.total_books += 1
        print(f"Book created: {self.title}")

    def __del__(self):
        Book.total_books -= 1
        print(f"Book deleted: {self.title}")


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        print(f"\nBooks in {self.name}:")
        for book in self.books:
            print(book.title)



b1 = Book("Python Basics", "John", 2022)
b2 = Book("MongoDB Guide", "David", 2023)
b3 = Book("Java Programming", "James", 2024)

lib = Library("Central Library")

lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

print("\nTotal books:", Book.total_books)
lib.list_books()


lib.books.remove(b2)
del b2


lib.list_books()

print("\nFinal count of books:", Book.total_books)

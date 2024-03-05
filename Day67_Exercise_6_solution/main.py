class Library:
    def __init__(self):
        self.noOfBooks = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.noOfBooks = len(self.books)

    def showInfo(self):
        print(f"The library has {self.noOfBooks} books and the books are")
        for book in self.books:
            print(book)

l1 = Library()

l1.addBook("Harry Potter Book 1")
l1.addBook("Harry Potter Book 2")
l1.addBook("Harry Potter Book 3")
l1.addBook("Harry Potter Book 4")

l1.showInfo()

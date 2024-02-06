# Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist the books after the program is stopped!

class Library:
    
    def __init__(self, number_of_books, books):
        self.number_of_books = number_of_books
        self.books = books

    def show_all_books(self, books):
        for book in books:
            print(book)

    def add_book(self):
        book_name =  input("\nEnter the name of the new book: ")
        books_list.append(book_name)

books_list = ['Triangle', 'circle', 'square']

lib_obj = Library(3, books_list)

lib_obj.show_all_books(books_list)
lib_obj.add_book()
lib_obj.show_all_books(books_list)
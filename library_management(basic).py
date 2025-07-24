#Write a Library class with no_of_books and books as two instance variables. Write a program to create
#a library from this Library class and show how you can print all books, add a book and get the number
#of books using different methods.
class Library:
   
    books = []
    no_of_books = 0

    def print_no_of_books(self):
        print(f"The library has {self.no_of_books}")

    def print_book_list(self):
        print(f"The books available are: {self.books}")

    def add_books(self,name):
        self.books.append(name)
        self.no_of_books = len(self.books)

obj1 = Library()
no_of_books = int(input("How many books do you want to add?"))
for i in range(no_of_books):
    book_name = input("Enter Book Name: ")
    obj1.add_books(book_name)
obj1.print_no_of_books()
obj1.print_book_list()





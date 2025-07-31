from os import system
if system("clear") != 0: system("cls")

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        self.is_available = True

    def __str__(self):
        return f"{self.title} by {self.author} - ${self.price:.2f}"

    def borrow(self):
        if not self.is_available:
            return f"'{self.title}' is currently not available."
        self.is_available = False
        return f"You have borrowed '{self.title}' by {self.author}."

    def return_book(self):
        self.is_available = True
        return f"You have returned '{self.title}' by {self.author}."

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book:Book):
        if not book.is_available:
            return f"Sorry, {self.name}. {book.title} is not available."

        book.borrow()
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book not in self.borrowed_books:
            return f"You haven't borrowed {book.title}."

        book.return_book()
        self.borrowed_books.remove(book)

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book:Book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def show_available_books(self):
        print("Available Books:")
        for book in self.books:
            if book.is_available:
                print(book.title)
    
    def register_user(self, user:User):
        if user in self.users:
            return f"User {user.name} is already registered."

        self.users.append(user)
        return f"User {user.name} registered successfully."

harry_potter = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 29.99)
lotr = Book("The Lord of the Rings", "J.R.R. Tolkien", 39.99)
python_book = Book("Learning Python", "Mark Lutz", 49.99)
clean_code = Book("Clean Code", "Robert C. Martin", 34.99)
algebra_baldor = Book("Álgebra Baldor", "Aurelio Baldor", 19.99)

gustavo = User("Gustavo", "12345")
claudia = User("Claudia", "67890")

library = Library()
library.add_book(harry_potter)
library.add_book(lotr)
library.add_book(python_book)
library.add_book(clean_code)
library.add_book(algebra_baldor)

library.register_user(gustavo)
library.register_user(claudia)

library.show_available_books()


gustavo.borrow_book(python_book)
gustavo.borrow_book(lotr)
claudia.borrow_book(harry_potter)
print(claudia.borrow_book(lotr))
print(claudia.borrow_book(python_book))
print(gustavo.borrow_book(harry_potter))
gustavo.return_book(python_book)
gustavo.return_book(lotr)
claudia.borrow_book(lotr)
claudia.borrow_book(python_book)

###
#  print(gustavo.borrowed_books)
#  print(claudia.borrowed_books)
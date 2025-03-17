# class Book:
#     def __init__(self, title, author, location):
#         self.title = title
#         self.author = author
#         self.location = location
#         self.page = 0
#
#     def turn_page(self, page):
#         self.page = page
#
# Refactor the provided code, so there is a separate class called Library,
# which contains books and has a method called find_book(title) that returns the book with the given title.
# Remove the unnecessary code from the Book class.

from typing import Dict


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


class Library:
    def __init__(self, books: Dict = {}):
        self.books = books  # {book: amount}

    def find_book(self, title: str) -> str:
        looking_for = next((x for x in self.books if x.title.lower() == title.lower()), None)
        if looking_for is None or self.books[looking_for] == 0:
            return f"{title} not available"
        return f"{looking_for.title} by {looking_for.author} is {looking_for.pages} pages long"

    def add_book(self, book: Book) -> None:
        if book not in self.books:
            self.books[book] = 0

        self.books[book] += 1

    def __str__(self):
        return '\n'.join(f'{x.title}: {y}' for x, y in self.books.items())


book1 = Book("Metro 2033", "Dmitry Glukhovsky", "544")
library = Library()
print(library)
library.add_book(book1)
print(library)
book2 = Book("The Left Hand of God", "Paul Hoffman", "448")
library.add_book(book2)
print(library)
library.add_book(book1)
print(library.find_book("the left hand of god"))

# class Book:
#     def __init__(self, content: str):
#         self.content = content
#
#
# class Formatter:
#     def format(self, book: Book) -> str:
#         return book.content
#
#
# class Printer:
#     def get_book(self, book: Book):
#         formatter = Formatter()
#         formatted_book = formatter.format(book)
#         return formatted_book

# We want to print books, but before printing the book, we should format it.
# To accomplish this, we have a class Printer that can print books and a class Formatter which is used by the Printer.
# Refactor the provided code that breaks the DIP because both the Printer and Formatter depend on concretions,
# not abstractions, by creating abstractions and injecting them wherever needed.
from abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter(ABC):
    @staticmethod
    @abstractmethod
    def format(book: Book):
        pass


class A4Formatter(Formatter):
    @staticmethod
    def format(book: Book):
        return book.content


class SomeOtherFormatter(Formatter):
    @staticmethod
    def format(book: Book):
        return book.content + book.content


class Printer:
    @staticmethod
    def get_book(book: Book, format_: Formatter):
        formatted_book = format_.format(book)
        return formatted_book


p = Printer()
f = SomeOtherFormatter()
b = Book("AbcbA")

print(p.get_book(b, f))

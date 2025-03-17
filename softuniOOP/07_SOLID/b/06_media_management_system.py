# You are developing a media management system that handles different types of media: Books, eBooks, and Audiobooks.
# The initial design violates several principles:
# the Single Responsibility Principle (SRP), the Open/Closed Principle (OCP), the Liskov Substitution Principle (LSP),
# and the Interface Segregation Principle (ISP) because it forces different media classes to implement methods
# irrelevant to their specific functionality.
# Specifically:
#   · Book is required to implement listen() even though it doesn't need this functionality.
#   · EBook is also required to implement listen() even though it should not have this method.
#   · Audiobook is required to implement read() even though it doesn't need this functionality.
# Tasks:
#   · Refactor the design by creating separate interfaces: Borrowable, Readable, and Listenable.
#   · Note that each book must be borrowed before it can be read or listened to.
from abc import ABC, abstractmethod


class Borrowable(ABC):
    @abstractmethod
    def borrow(self, user_id):
        pass


class Readable(Borrowable):
    @abstractmethod
    def read(self):
        pass


class Listenable(Borrowable):
    @abstractmethod
    def listen(self):
        pass


class Book(Readable):
    def __init__(self):
        self.borrowed = False
        self.progress = 0

    def borrow(self, user_id):
        self.borrowed = True
        print(f"Book borrowed by user {user_id}.")

    def read(self):
        if self.borrowed:
            self.progress += 10
            print(f"Reading the book. Progress: {self.progress}%")
        else:
            print("Book must be borrowed first.")


class EBook(Readable):
    def __init__(self):
        self.borrowed = False
        self.drm_applied = False
        self.progress = 0

    def borrow(self, user_id):
        self.borrowed = True
        self.drm_applied = True
        print(f"eBook borrowed by user {user_id}. DRM applied.")

    def read(self):
        if self.borrowed:
            self.progress += 20
            print(f"Reading the eBook. Progress: {self.progress}%")
        else:
            print("eBook must be borrowed first.")


class Audiobook(Listenable):
    def __init__(self):
        self.borrowed = False
        self.progress = 0

    def borrow(self, user_id):
        self.borrowed = True
        print(f"Audiobook borrowed by user {user_id}.")

    def listen(self):
        if self.borrowed:
            self.progress += 15
            print(f"Listening to the audiobook. Progress: {self.progress}%")
        else:
            print("Audiobook must be borrowed first.")


# test
book = Book()
book.borrow("user123")
book.read()
try:
    book.listen()
except AttributeError as e:
    print(e)
ebook = EBook()
ebook.borrow("user456")
ebook.read()
try:
    ebook.listen()
except AttributeError as e:
    print(e)
audiobook = Audiobook()
audiobook.borrow("user789")
audiobook.listen()
try:
    audiobook.read()
except AttributeError as e:
    print(e)
# output
# Book borrowed by user user123.
# Reading the book. Progress: 10%
# 'Book' object has no attribute 'listen'
# eBook borrowed by user user456. DRM applied.
# Reading the eBook. Progress: 20%
# 'EBook' object has no attribute 'listen'
# Audiobook borrowed by user user789.
# Listening to the audiobook. Progress: 15%
# 'Audiobook' object has no attribute 'read'


# old

# class Media:
#     def borrow(self, user_id):
#         pass
#
#     def read(self):
#         pass
#
#     def listen(self):
#         pass
#
# class Book(Media):
#     def __init__(self):
#         self.borrowed = False
#         self.progress = 0
#
#     def borrow(self, user_id):
#         self.borrowed = True
#         print(f"Book borrowed by user {user_id}.")
#
#     def read(self):
#         if self.borrowed:
#             self.progress += 10
#             print(f"Reading the book. Progress: {self.progress}%")
#         else:
#             print("Book must be borrowed first.")
#
#     def listen(self):
#         pass
#
# class EBook(Media):
#     def __init__(self):
#         self.borrowed = False
#         self.drm_applied = False
#         self.progress = 0
#
#     def borrow(self, user_id):
#         self.drm_applied = True
#         self.borrowed = True
#         print(f"eBook borrowed by user {user_id}. DRM applied.")
#
#     def read(self):
#         if self.borrowed:
#             self.progress += 20
#             print(f"Reading the eBook. Progress: {self.progress}%")
#         else:
#             print("eBook must be borrowed first.")
#
#     def listen(self):
#         pass
#
# class Audiobook(Media):
#     def __init__(self):
#         self.borrowed = False
#         self.progress = 0
#
#     def borrow(self, user_id):
#         self.borrowed = True
#         print(f"Audiobook borrowed by user {user_id}.")
#
#     def read(self):
#         pass
#
#     def listen(self):
#         if self.borrowed:
#             self.progress += 15
#             print(f"Listening to the audiobook. Progress: {self.progress}%")
#         else:
#             print("Audiobook must be borrowed first.")

# test
# book = Book()
# book.borrow("user123")
# book.read()
# book.listen() # No effect, but must be present
# ebook = EBook()
# ebook.borrow("user456")
# ebook.read()
# ebook.listen() # No effect, but must be present
# audiobook = Audiobook()
# audiobook.borrow("user789")
# audiobook.read() # No effect, but must be present audiobook.listen()
# output
# Book borrowed by user user123.
# Reading the book. Progress: 10%
# eBook borrowed by user user456. DRM applied.
# Reading the eBook. Progress: 20%
# Audiobook borrowed by user user789.
# Listening to the audiobook. Progress: 15%

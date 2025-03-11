# Write a function named classify_books that takes a variable number of arguments (tuples) and keyword arguments.
# The function is designed to help organize books into different genres and produce a sorted summary. The arguments will be passed as follows:
#  The first group of arguments will be an unknown number of tuples.
# o The first element in the tuple is the genre of the book (string). Each book belongs to one of two genres: "fiction" or "non_fiction".
# o The second element is the book's title (string). Each book title is unique.
#  The following group will be an unknown number of keyword arguments (key-value pairs).
# o Each key represents the unique ISBN (standardized book number as string).
# o Each value represents the title of the book (string).
# After receiving the information and calling the function:
#  Group the books into two categories:
# o Fiction books
# o Non-fiction books
#  Sort the books:
# o Fiction books should be sorted alphabetically in ascending order by ISBN.
# o Non-fiction books should be sorted alphabetically in descending order by ISBN.
#  Format the output as follows:
# o If there are fiction books, start with the heading: "Fiction Books:"
#  Prefix each book info with "~~~" (three tildes).
# o If there are non-fiction books, follow with the heading: "Non-Fiction Books:"
#  Prefix each book info with "***" (three asterisks).
# o If a category is empty, omit its heading entirely from the output. See the Examples section.
# In the end, return the output as described below.
# Output
#  The output should look like this (each string should be on a new line):
# o Fiction books are listed first (if any), followed by non-fiction books (if any).
# "Fiction Books:
# ~~~{ISBN1}#{book_title1}
# ...
# ~~~{ISBNn}#{book_titlen}
# Non-Fiction Books:
# ***{ISBN1}#{book_title1}
# ...
# ***{ISBNn}#{book_titlen}"
# Constraints
#  The arguments will always come before the keyword arguments.
#  Each tuple will contain a valid genre and book's title.
#  There will always be at least one tuple and keyword argument.
#  All book titles will be unique, and genres will always be valid ("fiction" or "non_fiction").
#  Each book will have a valid and unique ISBN.

def classify_books(*books, **books_again):
    to_return = ""

    fiction_books = {}
    non_fiction_books = {}

    for genre, book in books:
        for serail_num, buuk in books_again.items():
            if genre == "fiction" and buuk == book:
                fiction_books[serail_num] = book
            elif genre == "non_fiction" and buuk == book:
                non_fiction_books[serail_num] = book

    if fiction_books:
        to_return += "Fiction Books:\n"
    for x, y in sorted(fiction_books.items()):
        to_return += f"~~~{x}#{y}\n"

    if non_fiction_books:
        to_return += "Non-Fiction Books:\n"
    for x, y in sorted(non_fiction_books.items(), reverse=True):
        to_return += f"***{x}#{y}\n"

    return to_return

# 100/100

# test
print(classify_books(("fiction", "Brave New World"), ("non_fiction", "The Art of War"),
                     NF3421NN="The Art of War", FF1234UU="Brave New World"))

print(classify_books(("non_fiction", "The Art of War"), ("fiction", "The Great Gatsby"),
                     ("non_fiction", "A Brief History of Time"), ("fiction", "Brave New World"),
                     FF1234HH="The Great Gatsby", NF3845UU="A Brief History of Time",
                     NF3421NN="The Art of War", FF1234UU="Brave New World"))


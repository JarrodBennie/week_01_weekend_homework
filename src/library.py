def get_name(library):
    return library["name"]


def get_books(library):
    return library["books"]


def add_book(book, library):
    library["books"].append(book)


def remove_book(book, library):
    library["books"].remove(book)



def get_book_by_title(title, library):
    found_book = None
    for book in library["books"]:
        if book["title"] == title:
            found_book = book
    return found_book


# what is the function called?
# what parameters does it need?
# what does the function need to return?
# what does the function need to do?

def get_name(library):
    return library["name"]


def get_books(library):
    return library["books"]


def add_book(book, library):
    library["books"].append(book)


def remove_book(book, library):
    library["books"].remove(book)


# what is the function called?
# what parameters does it need?
# what does the function need to do?
# what does the function need to return?

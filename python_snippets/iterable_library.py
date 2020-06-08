class Library:
    def __init__(self, books=[]):
        self._books = books

    def __iter__(self):
        return (b for b in self._books)


class LibraryWithNext:
    def __init__(self, books=[]):
        self._books = books
        self._index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1
        if self._index >= len(self._books):
            self._index = -1
            raise StopIteration
        else:
            return self._books[self._index]


book_list = ['The Little Prince',
             'Animal Farm',
             'The Lord of the Flies']

library1 = Library(book_list)
library2 = LibraryWithNext(book_list)

for book in library1:
    print(book)

for book in library2:
    print(book)

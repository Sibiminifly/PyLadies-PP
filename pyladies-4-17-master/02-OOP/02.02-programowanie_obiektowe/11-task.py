'''
    Skopiuj kod z poprzedniego zadania. Do klasy Book dodaj
    atrybut klasowy books będący listą. Zmodyfikuj konstruktor,
    tak aby dodawać do niego każdy nowo tworzony obiekt klasy Book.
    Zmodyfikuj pętlę, tak żeby korzystać z nowo powstałej listy
    - atrybutu klasy.
'''
class Book:
    books = []

    def __init__(self, title, author, was_hardcover, price, pages, quantity):
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages
        self.was_hardcover = was_hardcover
        self.quantity = quantity
        Book.books.append(self)

if __name__=='__main__':
    for book_data in BOOKS_LIST:
        book = Book(**book_data)

    Book.books[]
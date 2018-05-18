'''
    Skopiuj tutaj kod z rozwiązania zadania z pliku 06, 
    a następnie zmodyfikuj go dodając do klasy Book metodę
    is_available(), która zwróci wartość logiczną w zależności
    od tego, czy dostępne są egzemplarze danej ksiązki.
    W pętli printującej reprezentację tekstową książki zmień kod tak,
    aby na ekranie pojawiła się informacja o dostępności danej ksiązki.
'''


class Book:
    def __init__(self, autor, tytul, cena, ilosc_stron, ilosc_ksiazek, czy_w_twardej_okladce):
        self.autor_name = autor
        self.title = tytul
        self.price = cena
        self.pages = ilosc_stron
        self.ilosc = ilosc_ksiazek
        self.rodzaj_okladki = czy_w_twardej_okladce

    def __str__(self):
        return '{tytul} by {autor}'.format(
            tytul=self.title,
            autor=self.autor_name)
    def is_available(self):
        if self.ilosc > 1:
            return True
        else:
            return False


if __name__ == '__main__':
    book = Book(
        autor="Lackberg",
        tytul="Bekart",
        cena=23.50,
        ilosc_stron=165,
        ilosc_ksiazek=4,
        czy_w_twardej_okladce=False,
    )
    print(book.title)
    print(book.autor_name)
    print(book.price)
    print(book.pages)
    print(book.ilosc)
    print(book.rodzaj_okladki)
    print("Czy ksiazka jest dostepna", book.is_available())
'''
    Twoim zadaniem jest stworzenie programu do zarządzania
    księgarnią - bez wątpienia przydałaby się w nim klasa 
    reprezentująca książki. Zastanów się jak moglaby wyglądać, 
    a następnie zaimplementuj ją w tym pliku (nie zapomnij o 
    konstruktorze!). Na koniec stwórz w pętli 3 instancji tej 
    klasy wykorzystując dane we wcześniej przygotowanejliście
    słowników (podobnej do listy z pliku 01) i **kwargsy.
    Każdą z tych instancji dołącz do listy, po czym przeiteruj się
    po tej liście i dla każdej ksiązki wyprintuj jej tytuł.
'''
class Book:
    def __init__(self, autor, tytul, cena, ilosc_stron,ilosc_ksiazek, czy_w_twardej_okladce):
        self.autor_name = autor
        self.title = tytul
        self.price = cena
        self.pages = ilosc_stron
        self.ilosc = ilosc_ksiazek
        self.rodzaj_okladki = czy_w_twardej_okladce
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


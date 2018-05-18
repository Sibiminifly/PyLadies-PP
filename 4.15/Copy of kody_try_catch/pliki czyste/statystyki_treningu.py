# słownik inicjały zawodników na nazwiska
zawodnicy = dict([('mk', 'Michał Kowalski'), ('pk', 'Paweł Kawa'), ('dj', 'Dawid Jachnik')])
print(zawodnicy)
# tu dla każdego zawodnika przechowujemy listę czasów okrążeń w wartości słownika pod inicjałami jako kluczem
zawodnicy_okrazenia = dict()
for zaw in zawodnicy:
    zawodnicy_okrazenia[zaw] = []
# Aż nie wpiszemy EXIT wykonuj pętlę:
while True:
    print('Podaj inicjały i, po spacji, czas okrążenia. Jeśli chcesz wyjść, wpisz EXIT')
    wejscie = input()
    # czy zakończyć pętlę?
    if wejscie == 'EXIT':
        # wyskakujemy z while!
        break
    # rozbijamy wiersz po białych znakach i przypisujemy do dwóch zmiennych
    # to co przed spacją do zmiennej inicjaly, to co po spacji do zmiennej czas
    inicjaly, czas = wejscie.split()
    # zapisujemy czas okrążenia dla zawodnika!
    zawodnicy_okrazenia[inicjaly].append(float(czas))
# wypisanie statystyk
print('Podsumowanie:')
# iterujemy po poszczególnych zawodnikach
# dla każdego wypisujemy nazwisko, średnio czas okrążenia i liczbę okrążeń
for zaw in zawodnicy:
    print('Zawodnik:', zawodnicy[zaw])
    print('\tŚredni czas okrążenia:', sum(zawodnicy_okrazenia[zaw]) / len(zawodnicy_okrazenia[zaw]))
    print('\tLiczba okrążeń:', len(zawodnicy_okrazenia[zaw]))
print('Program zakończył się sukcesem. Dzięki!')

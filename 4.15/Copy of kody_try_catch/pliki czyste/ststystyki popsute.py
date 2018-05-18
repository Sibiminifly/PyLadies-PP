# słownik (przechowuje parę: klucz i wartość) inicjały zawodników na nazwiska; tuple = krotka (uporządkowana kolekcja jak lista, tylko nie można tego zmieniać)
zawodnicy = dict([('mk', 'Michał Kowalski'), #w kazdej krotce 1-szy element będzie kluczem, a 2gi wartością
                  ('pk', 'Paweł Kawa'),
                  ('dj', 'Dawid Jachnik')]
                 )
print(zawodnicy['mk'])
print(zawodnicy)
# tu dla każdego zawodnika przechowujemy listę czasów okrążeń w wartości słownika pod inicjałami jako kluczem
zawodnicy_okrazenia = dict() #tworzę pusty słownik; chcę aby pod spodem była lista długości kolejnych okrążeń
#np piszę 'mk' = [9.8, 10,11, 2.03]
#           'pk' = [...,..]
#dict -->słownik
for zaw in zawodnicy: #for zmienna in słownik
    zawodnicy_okrazenia[zaw] = [] #dla każdego słownika tworzę pustą listę
# Aż nie wpiszemy EXIT wykonuj pętlę:
while True: #pętla wykonuje się tak długo aż warunek będzie prawdziwy; chyba, że w środku będzie miała break
    try:
            print('Podaj inicjały i, po spacji, czas okrążenia. Jeśli chcesz wyjść, wpisz EXIT')
            wejscie = input()
            # czy zakończyć pętlę?
            if wejscie == 'EXIT': #sprawdzamy czy liczby są sobie równe ==
                # wyskakujemy z while!
                break
            # rozbijamy wiersz po białych znakach i przypisujemy do dwóch zmiennych
            # to co przed spacją do zmiennej inicjaly, to co po spacji do zmiennej czas
            inicjaly, czas = wejscie.split() #przypisujemy dwie zmienne do listy
        # split to metoda, która dzieli łańcuch znaków po białych znakach na listę
        #'szedłem i małem".split()
        #['szedłem' 'i' 'miałem']
            # zapisujemy czas okrążenia dla zawodnika!
            zawodnicy_okrazenia[inicjaly].append(float(czas)) #append dodaje coś do tej listy; float to liczba zmiennoprzecinkowa
        # wypisanie statystyk
    except KeyError as ex:#jeśli wpiszę ex do printa to wypisze mi błąd jaki pojawia się
        #jeśli wpiszę exceptKeyError in ex: to mi wpisze tylko ten typ błędu
        #jeśli wpiszę Exeption as ex: wypisze mi każdy typ błędu
        print('Nie ma takiego zawodnika. głuptasku!')
        #dla dowolnego typu błędu mogę wypisać kilka exceptów
    except:
        print('Nieoczekiwany błąd. Nie wiem co się stało')
#        print('Coś poszło nie tak')
#        print(ex)#mogę wyłapywać określone typy wyjątków np Key Error, Value Error
#        print('Spóbuj jeszcze raz')
#wypisywanie statystyk
print('Podsumowanie:')
# iterujemy po poszczególnych zawodnikach
# dla każdego wypisujemy nazwisko, średnio czas okrążenia i liczbę okrążeń
#suma([2,4,6]) daje sumę
#len([2,4,6]) daje liczbę ile razy coś występuje; długość listy
for zaw in zawodnicy:
    print('Zawodnik:', zawodnicy[zaw])
    print('\tŚredni czas okrążenia:', sum(zawodnicy_okrazenia[zaw]) / len(zawodnicy_okrazenia[zaw]))
    print('\tLiczba okrążeń:', len(zawodnicy_okrazenia[zaw]))
print('Program zakończył się sukcesem. Dzięki!')
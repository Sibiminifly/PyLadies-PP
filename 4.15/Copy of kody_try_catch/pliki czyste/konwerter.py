"""
Prosty moduł do konwersji jednostek
Główną funkcją jest unit_converter, która przyjmuje wartośc i kody dwóch jednostek
Na tej podstawie zwraca odpowiednią wartość lub wyrzuca wyjątek, jeśli konwersja się nie powiodła
"""

# definicje możliwych do wygenerowania wyjątków
class IncompatibleUnitsException(Exception):
    # wyjątek wyrzucany, gdy np. chcemy przekonwertować centrymetry na stopnie celcjusza
    pass

class UnknownUnitException(Exception):
    # wyjątek wyrzucany, gdy dostaliśmy nieznaną jednostkę
    pass

# kody, za pomocą których odnosimy się do poszczególnych jednostek
KELVIN = 'K' #programista informuje aby te zmienne nie były zmieniane dlatego są z wielkiej litery
CELCIUS = 'C'
CENTIMETER = 'cm'
INCH = 'in'
YARD = 'yd'
# lista wszystkich jednostek; za jej pomocą mając kod jednostki możemy sprawdzać
# czy ta jednostka jest stała
# np. 'F' in KNOWN_UNITS da wartość false (nie mamy zaimplementowanej obsługi stopni fahrenheita)
KNOWN_UNITS = [KELVIN, CELCIUS, CENTIMETER, INCH, YARD]


def unit_converter(value, unit_from, unit_to):
    """
    Funkcja dokonuje żądanej konwersji lub zwraca wyjątek, jeśli konwersja nie jest możliwa
    :param value: Wartość, którą chcemy przekonwertować
    :param unit_from: z jakiej jednostki konwertujemy
    :param unit_to: na jaką jednostkę konwertujemy
    :return: przekonwertowana wartość
    """
    # sprawdzamy, czy znamy nadesłane jednostki
    # jeśli nie, wtedy nie wiemy co właściwie mamy konwertować; nie możemy wykonać operacji!
    # w związku z tym zgłaszamy wyjątek
    if unit_from not in KNOWN_UNITS:#raise podaje jaki typ wyjątku został wygenerowany; piszę reise i podaję typ wyjątku, nawet zdefinowanego prze zmnie
        raise UnknownUnitException("Unknown unit: {0}. Known units are: {1}".format(unit_from,KNOWN_UNITS))
    if unit_to not in KNOWN_UNITS:
        raise UnknownUnitException("Unknown unit: {0}. Known units are: {1}".format(unit_to, KNOWN_UNITS))
    # jesli konwersja jednostki sama na siebie - zwracamy nadesłaną wartość
    if  unit_from == unit_to:
        return value
    # stąd - jedziemy z poszczególnymi znanymi wariantami konwersji i wywołujemy odpowiednie funkcje
    if unit_from == KELVIN and unit_to == CELCIUS:
        return kelvin_to_celcius(value)
    elif unit_from == CELCIUS and unit_to == KELVIN:
        return celcius_to_kelvin(value)
    elif unit_from == CENTIMETER and unit_to == INCH:
        return cm_to_inches(value)
    elif unit_from == INCH and unit_to == CENTIMETER:
        return inches_to_cm(value)
    elif unit_from == CENTIMETER and unit_to == YARD:
        return cm_to_yard(value)
    elif unit_from == YARD and unit_to == CENTIMETER:
        return yard_to_cm(value)
    elif unit_from == YARD and unit_to == INCH:
        return yard_to_inch(value)
    elif unit_from == INCH and unit_to == YARD:
        return inch_to_yard(value)
    else:
        # jeśli kombinacja jednostek unit_from - unit_to nie została złapana przez żaden z ifów powyżej...
        # to znaczy, że nie da się między nimi przeprowadzić konwersji
        # np. nie mogę przekonwertować centymetrów na stopnie celcjusza!
        # nie mogę zwrócić żadnej wartości, wyrzucam więc wyjątek
        raise IncompatibleUnitsException('Cannot convert {0} to {1}'.format(unit_from, unit_to))


"""
DEFINICJE POSZCZEGÓLNYCH METOD PRZEPROWADZAJĄCYCH KONWERSJE POMIĘDZY OKREŚLONYMI PARAMI JEDNOSTEK
"""

def cm_to_inches(value):
    return value * 0.393700787

def inches_to_cm(value):
    return value * 2.54

def cm_to_yard(value):
    return value * 0.010936133

def yard_to_cm(value):
    return 91.44 * value

def celcius_to_kelvin(value):
    return value + 273.15

def kelvin_to_celcius(value):
    return value - 273.15

def yard_to_inch(value):
    return 36 * value

def inch_to_yard(value):
    return value / 36

if __name__ == '__main__':
    # ten kod (dzięki powyższemu ifowi )wywoła się tylko, jeśli ten plik jest odpalany jako główny
    # np. jak zrobię python konwerter.py, ten kod się odpali
    # jeśli zaś ten plik zaimportuję jako moduł - if się nie odpali, kod poniżej zostanie pominięty!
    while True:
        print('Wpisz wartość, jaką chcesz przekonwertować (bez jednostek). Jesli chcesz zakończyć, wpisz EXIT')
        val = input()
        if val.upper() == 'EXIT':
            break
        val = float(val)
        print('Z jakiej jednostki? Możliwe to', KNOWN_UNITS)
        ufrom = input()
        print('Na jaką jednostkę? Możliwe to', KNOWN_UNITS)
        uto = input()
        print('Wynik:')
        print(unit_converter(val, ufrom, uto))
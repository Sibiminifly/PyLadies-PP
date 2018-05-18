#print('Hellow world')
#print(2/5)
#a = 0
#if a != 0:
#    b = 2/a
#else:
#    print('Nie da sie podzielic')
#    b = None
#print('Koniec programu', b)


# to jest 1-sza najważniejsza reguła
print('Hellow world')
try:
    print(2/5)
    a = 0
    b = 2/a
    print('Udało się podzielić!')
    print('Udało się podzielić!')
except:
    print('Ups! Coś nie tak')
    b = None
print('Koniec programu', b)
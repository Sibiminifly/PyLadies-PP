def funkcja_z_bledem():
    try:
        print('wszedlem do funkcji')
        [1,2,3][9868]
        print('udalo sie')
        return'koniec'
    except:
        print('nic')
print('Poczatek programu')
try:
    funkcja_z_bledem()
except IndexErroras as ex:
    print('Chyba nie było tego elementu')
print('Koniec programu')
#data loadin = do_4.19

from data_loading import load_data
DATA_PATH = './szwagropol_data/transactions.txt'
column, rows = load_data(DATA_PATH)
from helper_functions import parse_date_from_string


def load_data(path):
    with open(DATA_PATH, encoding='utf-8') as f:
    #każdy plik trzeba zamknąć po użyciu, with zapewnia,
    # że jak otworzymy plik to on się później automatycznie zamknie i nie trzeba później robić close
        rows = []
        columns = f.readline().strip().split(';')
        for line in f:
            current_row = line.strip().split(';')# możemy podzielić splitem
            current_row[0] = parse_date_from_string(current_row[0])
            current_row[-2] = int(current_row[-2])
            try:
                current_row[-1] = float(current_row[-1])
            except ValueError:
                continue
            rows.append(current_row)
            return columns, rows
    for i in range(5):
        print(rows[i])

#D:\PyLadies\Pyladies_4.19_Projekt-master\szwagropol_data\transactions.txt

#transaction_time  (rok-miesiac-dzien godzina:minuta:sekunda)
#customer -  (tak klientów identyfikuje szwagropol)
#product_name -
#category_name -  (jedna z: Beverages, Dairy Products, Confections, Seafood,
#Condiments, Grains/Cereals, Meat/Poultry, Produce, Luxury)
#quantity
#unit_price - cena/szt


#############################################
#import matplotlib.pyplot as plt
#plt.plot([1, 2, 3, 4], [1, 2, 3, 4])
#plt.ylabel('some numbers')
#plt.show()

import matplotlib.pyplot as plt
plt.bar([1, 2, 3, 4, 5], revenues)
plt.show()
##
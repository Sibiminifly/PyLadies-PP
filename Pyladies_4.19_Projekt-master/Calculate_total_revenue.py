from data_loading import load_data

DATA_PATH = './szwagropol_data/transactions.txt'
TRANSACTIONS_TIME_INDEX = 0
CUSTOMER_INDEX = 1
PRODUCTION_NAME_INDEX = 2
CATEGORY_NAME_INDEX = 3
QUANTITY_INDEX = 4
UNITY_PRICE_INDEX = 5
TOTAL_VALUE = 6

columns, rows = load_data(DATA_PATH)

columns.append('total_transaction_values')

for row in rows:
    total = row[QUANTITY_INDEX]*row[UNITY_PRICE_INDEX]
    row.append(total)
#dla każdego wiersza pomnośyć ilość produktó razy cena
total_revenue = 0
for row in rows:
    total_revenue += row[TOTAL_VALUE]
#dodaj do wyniku ostatnią wartość w liście

print(total_revenue)
#for i in range(5):
#    print(rows[i])



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
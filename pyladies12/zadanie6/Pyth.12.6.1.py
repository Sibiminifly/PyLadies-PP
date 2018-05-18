import requests  # alt enter na tym opcja do doinstalowania
import json

url = 'https://rickandmortyapi.com/api/character/'

response = requests.get(url)

if response.status_code == 200:
    #    json.loads(response.text)
    #heroes_list = response.json().get('results')
    json_file = open('data.json') #dla tych co nie mają Internetu
    heroes_list1 = json.load(json_file)
    json_file.close()

    results_list = []

    for hero in heroes_list:
        #        for keys in hero:
        hero_info = {
            'name': hero['name'],  # tworzy nowy słownik. do klucza name przypisuje wartość
            'species': hero['species'],
            'gender': hero['gender'],
            'image': hero['image']
        }

        results_list.append(hero_info)
    fp = open('heroes.json', 'w+')
    json.dump(results_list, fp)
    fp.close()
    #    print(heroes_list)
    #    heroes = response.json().get('results')

    # otwieramy plik heroes.json i klikamy Ctrl+alt+L

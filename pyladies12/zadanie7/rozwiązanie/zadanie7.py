import requests

url = 'https://rickandmortyapi.com/api/character/'
response = requests.get(url)
if response.status_code == 200:
    heroes = response.json().get('results')

    fp = open('html\\hero-template.html')
    hero_template = fp.read()
    fp.close()

    new_heroes_html = []
    for hero in heroes:
        hero_image = hero.get('image', '#')
        hero_status = hero.get('status', 'alive').lower()
        hero_name = hero.get('name', 'Unknown')
        hero_race = hero.get('species', 'Human')

        formatted_hero_template = hero_template.format(hero_image=hero_image, hero_name=hero_name, hero_race=hero_race,
                                                       hero_status=hero_status)
        new_heroes_html.append(formatted_hero_template)

    fp = open('html\\index-template.html')
    page_template = fp.read()
    fp.close()

    body = ''.join(new_heroes_html)
    page_template = page_template.format(body=body)

    fp = open('index.html', 'w+')
    fp.write(page_template)
    fp.close()

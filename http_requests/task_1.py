import requests

base_url = 'https://www.superheroapi.com/api.php/2619421814940190/'


def get_character_id_by_name(name):
    url = f'{base_url}search/{name}'
    resp = requests.get(url)
    if resp.status_code == 200:
        for character in resp.json()['results']:
            if character['name'] == name:
                return character['id']
    else:
        raise Exception('ID персонажа не найдено')


def get_intelligence_by_id(id):
    url = f'{base_url}{id}/powerstats'
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json()['intelligence']


def compare_intelligence_by_name(names=[]):
    intelligence_name = {}
    for name in names:
        id_character = get_character_id_by_name(name)

        intelligence_character = get_intelligence_by_id(id_character)

        intelligence_name[name] = int(intelligence_character)

    return max(intelligence_name, key=intelligence_name.get)


print(compare_intelligence_by_name(['Hulk', 'Captain America', 'Thanos']))

import json

with open(
        'peliculas_genero_separado.json') as f:
    json_films = json.load(f)
    dict_films = {}
    for id, film in json_films.items():
        dict_films[id] = {word:True for word in film}

    with open('peliculas_genero_separado_dict.json', 'w') as fw:
        json.dump(dict_films, fw)



import json
'''d
with open(
        'C:\\Users\JAVI\PycharmProjects\Sistemas-Int\Sist.-Inteligentes\Dataset\peliculas_genero_separado.json') as f:
    json_films = json.load(f)
    dict_films = {}
    for id, film in json_films.items():
        dict_films[id] = {word:True for word in film}

    with open('C:\\Users\JAVI\PycharmProjects\Sistemas-Int\Sist.-Inteligentes\Dataset\peliculas_genero_separado_dict.json', 'w') as fw:
        json.dump(dict_films, fw)
'''
from scipy.spatial.distance import cosine


def remove_common_keys_from_dict1(nand_op_film, film_vector):
    common_keys = nand_op_film.copy()
    for key in common_keys.keys():
        nand_op_film.pop(key)
        film_vector.pop(key)




with (open(
        'C:\\Users\JAVI\PycharmProjects\Sistemas-Int\Sist.-Inteligentes\Dataset\TF-IDF.json') as tf_idf):
    vectors = json.load(tf_idf)
    current_film_vector = vectors['23']

    similarities = []

    for id, other_film_vector in vectors.items():
        if (id == '23'):
            curr_film_array = []
            other_film_array = []

            #Almacenarán las palabras ya usadas para borrarlas luego de cada diccionario
            nand_op_curr_film = {}
            nand_op_other_film = {}

            for word, val in current_film_vector.items():
                if word in other_film_vector:
                    other_film_array.append(other_film_vector[word])
                    nand_op_other_film[word] = -999
                else:
                    other_film_array.append(0)
                curr_film_array.append(val)
                nand_op_curr_film[word] = -999

            #eliminación de las palabras usadas
            remove_common_keys_from_dict1(nand_op_curr_film, current_film_vector)
            remove_common_keys_from_dict1(nand_op_other_film, other_film_vector)
            print("oth: "+str(other_film_vector))
            for word, val in other_film_vector.items():
                if word in current_film_vector:
                    curr_film_array.append(current_film_vector[word])
                    nand_op_curr_film[word] = -999
                else:
                    curr_film_array.append(0)
                other_film_array.append(val)
                nand_op_other_film[word] = -999

            print("curr: "+current_film_vector)
            print("other: "+other_film_vector)



            sim = 1-cosine(curr_film_array, other_film_array)
            similarities.append((id, sim))

    #similarities.sort(key=lambda cos_sim: cos_sim[1])

    print(similarities)




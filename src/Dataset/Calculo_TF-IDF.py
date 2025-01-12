import json
import math

tf = {}
idf = {}

with open(
        'C:\\Users\\JAVI\\PycharmProjects\\Sistemas-Int\\Sist.-Inteligentes\\src\Dataset\\peliculas_consensus_separado.json') as f:
    json_data = json.load(f)
    N = len(json_data)
    for key, item in json_data.items():
        aux_bag = {}
        already_found_bag = {}
        for word in item:
            if not already_found_bag.get(word):
                if idf.get(word):
                    idf[word] += 1
                else:
                    idf[word] = 1
            already_found_bag[word] = True

            if aux_bag.get(word):
                aux_bag[word] += 1
            else:
                aux_bag[word] = 1
        tf[key] = aux_bag

    tf_idf = {}
    for key, item in tf.items():
        aux_bag = {}
        for word, word_value in item.items():
            aux_bag[word] = word_value*math.log(N/idf.get(word),10)
        tf_idf[key] = aux_bag

    with open('TF-IDF.json', 'w') as fw:
        json.dump(tf_idf, fw)
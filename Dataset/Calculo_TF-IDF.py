import json

tf = {}
idf = {}

with open(
        'C:\\Users\JAVI\PycharmProjects\Sistemas-Int\Sist.-Inteligentes\Dataset\peliculas_synopsis_separado.json') as f:
    json_data = json.load(f)
    for key, item in json_data.items():
        aux_bag = {}
        for word in item:
            if idf.get(word):
                idf[word] += 1
            else:
                idf[word] = 1

            if aux_bag.get(word):
                aux_bag[word] += 1
            else:
                aux_bag[word] = 1
        tf[key] = aux_bag
    tf_idf = {}
    for key, item in tf.items():
        aux_bag = {}
        for word, word_value in item.items():
            aux_bag[word] = word_value/idf.get(word)
        tf_idf[key] = aux_bag

    with open('C:\\Users\JAVI\PycharmProjects\Sistemas-Int\Sist.-Inteligentes\Dataset\TF-IDF.json', 'w') as fw:
        json.dump(tf_idf, fw)
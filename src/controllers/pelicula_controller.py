from models.pelicula import PeliculaModel
import json
from scipy.spatial.distance import cosine

class PeliculaController:
    def __init__(self):
        self.modelo_pelicula = PeliculaModel()
        
    def obtener_peliculas(self):
        """Obtiene todas las películas."""
        return self.modelo_pelicula.mostrar_peliculas()

    def obtener_info_pelicula(self, id_pelicula):
        """Obtiene los datos de la película seleccionada."""
        return self.modelo_pelicula.obtener_pelicula_por_id(id_pelicula)

    def remove_common_keys_from_dict1(self,nand_op_film, film_vector):
        common_keys = nand_op_film.copy()
        for key in common_keys.keys():
            nand_op_film.pop(key)
            if key in film_vector.keys():
                film_vector.pop(key)

    def obtener_similares(self, id_pelicula):
        """Obtiene películas similares."""
        with open(
                'Dataset/TF-IDF.json') as tf_idf:
            vectors = json.load(tf_idf)
            similarities = []
            for id, other_film_vector in vectors.items():
                current_film_vector = vectors[str(id_pelicula)].copy()
                if (id != str(id_pelicula)):
                    curr_film_array = []
                    other_film_array = []

                    # Almacenarán las palabras ya usadas para borrarlas luego de cada diccionario
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

                    # eliminación de las palabras usadas
                    self.remove_common_keys_from_dict1(nand_op_curr_film, current_film_vector)
                    self.remove_common_keys_from_dict1(nand_op_other_film, other_film_vector)

                    for word, val in other_film_vector.items():
                        if word in current_film_vector:
                            curr_film_array.append(current_film_vector[word])
                            nand_op_curr_film[word] = -999
                        else:
                            curr_film_array.append(0)
                        other_film_array.append(val)
                        nand_op_other_film[word] = -999
                    sim = 1 - cosine(curr_film_array, other_film_array)
                    similarities.append((id, sim))

            similarities.sort(reverse=True, key=lambda cos_sim: cos_sim[1])
            most_simmilars = []
            for i in range(0, 10):
                most_simmilars.append(similarities[i][0])
            print("Películas más similares a "+str(id_pelicula)+": "+str(most_simmilars))
            data = self.modelo_pelicula.obtener_peliculas_similares(most_simmilars)
            return data

    #??
    def obtener_pelicula_por_id(self, id_pelicula):
        """Obtiene los datos de una película específica por su ID."""
        return self.modelo_pelicula.obtener_pelicula_por_id(id_pelicula)
    
        
    def contar_valoraciones_usuario(self, id_usuario):
        """Cuenta cuántas valoraciones tiene un usuario."""
        return self.modelo_pelicula.contar_valoraciones_usuario(id_usuario)
        
    def verificar_valoraciones_usuario(self, id_usuario):
        """Verifica si el usuario tiene menos de 10 valoraciones."""
        return self.modelo_pelicula.contar_valoraciones_usuario(id_usuario)

    def obtener_pelicula_aleatoria(self):
        """Obtiene una película aleatoria."""
        return self.modelo_pelicula.obtener_pelicula_aleatoria()

    def guardar_valoracion(self, id_usuario, id_pelicula, valoracion):
        """Guarda la valoración de una película."""
        print(f"[DEBUG] Guardando valoración: Usuario {id_usuario}, Película {id_pelicula}, Valoración {valoracion}")
        self.modelo_pelicula.guardar_valoracion(id_usuario, id_pelicula, valoracion)

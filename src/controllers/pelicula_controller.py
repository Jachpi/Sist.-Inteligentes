from models.pelicula import PeliculaModel
import json


class PeliculaController:
    def __init__(self):
        self.modelo_pelicula = PeliculaModel()
        
    def obtener_peliculas(self):
        """Obtiene todas las películas."""
        return self.modelo_pelicula.mostrar_peliculas()

    def obtener_info_pelicula(self, id_pelicula):
        """Obtiene los datos de la película seleccionada."""
        return self.modelo_pelicula.obtener_pelicula_por_id(id_pelicula)

    def obtener_similares(self, id_pelicula):
        """Obtiene películas similares."""
        with open(
                'C:\\Users\JAVI\PycharmProjects\Sistemas-Int\Sist.-Inteligentes\Dataset\peliculas_genero_separado_dict.json') as tf_idf:
            vectors = json.load(tf_idf)
            current_film_vector = vectors[id_pelicula]
            for id, vector in vectors.items():
                print(current_film_vector & vector)
                if (id != id_pelicula):
                    pass




    def sorcen_dice(self, usuario_bag, pelicula_bag):
        return 2 * len(usuario_bag.keys() & pelicula_bag.keys()) / (
                    len(pelicula_bag.keys()) + len(usuario_bag.keys()))

    #javier@javier.com

    def obtener_pelicula_por_id(self, id_pelicula):
        """Obtiene los datos de una película específica por su ID."""
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, title, year, synopsis, genre, img
                FROM peliculas WHERE id = ?
            """, (id_pelicula,))
            return cursor.fetchone()

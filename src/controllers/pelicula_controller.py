from models.pelicula import PeliculaModel

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
        return self.modelo_pelicula.obtener_peliculas_similares(id_pelicula)
    
    def obtener_pelicula_por_id(self, id_pelicula):
        """Obtiene los datos de una película específica por su ID."""
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, title, year, synopsis, genre, img
                FROM peliculas WHERE id = ?
            """, (id_pelicula,))
            return cursor.fetchone()

from models.pelicula import PeliculaModel

class MenuController:
    def __init__(self):
        self.modelo_pelicula = PeliculaModel()

    def obtener_peliculas(self):
        """Obtiene todas las películas desde el modelo."""
        return self.modelo_pelicula.mostrar_peliculas()

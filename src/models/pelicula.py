import sqlite3

class PeliculaModel:
    def __init__(self, db_path="peliculas.db"):
        self.db_path = db_path

    def conectar(self):
        """Establece conexión con la base de datos."""
        return sqlite3.connect(self.db_path)

    def mostrar_peliculas(self):
        """Obtiene todas las películas de la base de datos."""
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM peliculas")
            return cursor.fetchall()

    def mostrar_peliculas_procesadas(self):
        """Obtiene todas las películas de la base de datos."""
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM peliculas_procesado")
            return cursor.fetchall()

    def obtener_pelicula_por_id(self, id_pelicula):
        """Obtiene los datos de una película específica por su ID."""
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM peliculas WHERE id = ?", (id_pelicula,))
            return cursor.fetchone()

    def obtener_peliculas_similares(self, id_pelicula):
        """
        Simula la búsqueda de películas similares.
        Por ahora solo devuelve 5 películas distintas a la seleccionada.
        """
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM peliculas
                WHERE id != ?
                ORDER BY people_score
                LIMIT 10
            """, (id_pelicula,))
            return cursor.fetchall()

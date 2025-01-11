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

    def obtener_peliculas_similares(self, ids_peliculas):
        """
        Simula la búsqueda de películas similares.
        Por ahora solo devuelve 5 películas distintas a la seleccionada.
        """
        with self.conectar() as conn:
            cursor = conn.cursor()
            placeholders = ', '.join('?' for id in ids_peliculas)
            query = f"SELECT * FROM peliculas WHERE id IN ({placeholders})"
            cursor.execute(query, ids_peliculas,)
            return cursor.fetchall()
        
    def contar_valoraciones_usuario(self, id_usuario):
        """Cuenta cuántas valoraciones tiene un usuario."""
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM valoraciones WHERE id_usuario = ?", (id_usuario,))
            return cursor.fetchone()[0]

    def obtener_pelicula_aleatoria(self):
        """Obtiene una película aleatoria de la base de datos."""
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM peliculas ORDER BY RANDOM() LIMIT 1")
            return cursor.fetchone()

    def guardar_valoracion(self, id_usuario, id_pelicula, valoracion):
        """Guarda la valoración de un usuariogit  para una película."""
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO valoraciones (id_usuario, id_pelicula, valoracion) VALUES (?, ?, ?)",
                (id_usuario, id_pelicula, valoracion),
            )
            conn.commit()

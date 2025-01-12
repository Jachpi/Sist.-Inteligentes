import sqlite3

class PeliculaModel:
    def __init__(self, db_path="peliculas.db"):
        self.db_path = db_path

    def conectar(self):
        """Establece conexión con la base de datos y habilita claves foráneas."""
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON")  # Activa claves foráneas
        return conn


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
        """
        with self.conectar() as conn:
            cursor = conn.cursor()
            placeholders = ', '.join('?' for id in ids_peliculas)
            query = f"SELECT * FROM peliculas WHERE id IN ({placeholders})"
            cursor.execute(query, ids_peliculas,)
            return cursor.fetchall()
        

    def obtener_pelicula_aleatoria(self):
        """Obtiene una película aleatoria de la base de datos."""
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM peliculas ORDER BY RANDOM() LIMIT 1")
            resultado = cursor.fetchone()
            return resultado

    def obtener_peliculas_bien_valoradas(self, id_usuario):
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM valoraciones WHERE id_usuario = ? AND valoracion > 2"
                           " ORDER BY id_valoracion LIMIT 30", (id_usuario,))
            return cursor.fetchall()

    def guardar_valoracion(self, id_usuario, id_pelicula, valoracion):
        """Guarda la valoración de un usuario para una película."""
        try:
            with self.conectar() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO valoraciones (id_usuario, id_pelicula, valoracion)
                    VALUES (?, ?, ?)
                """, (id_usuario, id_pelicula, valoracion))
                conn.commit()
                print("[DEBUG] Valoración guardada correctamente.")
        except sqlite3.IntegrityError as e:
            print(f"[ERROR] Error de integridad al guardar la valoración: {e}")
        except Exception as e:
            print(f"[ERROR] Error inesperado al guardar la valoración: {e}")

    def obtener_valoracion(self, id_usuario, id_pelicula):
        """Consulta si existe una valoración previa."""
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT valoracion FROM valoraciones
                WHERE id_usuario = ? AND id_pelicula = ?
            """, (id_usuario, id_pelicula))
            resultado = cursor.fetchone()
            return resultado[0] if resultado else None

    def actualizar_valoracion(self, id_usuario, id_pelicula, nueva_valoracion):
        """Actualiza la valoración existente."""
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE valoraciones
                SET valoracion = ?
                WHERE id_usuario = ? AND id_pelicula = ?
            """, (nueva_valoracion, id_usuario, id_pelicula))
            conn.commit()
            
            
    def obtener_valoracion(self, id_usuario, id_pelicula):
        """Obtiene la valoración existente de un usuario para una película."""
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT valoracion FROM valoraciones
                WHERE id_usuario = ? AND id_pelicula = ?
            """, (id_usuario, id_pelicula))
            resultado = cursor.fetchone()
            return resultado[0] if resultado else None

    def contar_valoraciones_usuario(self, id_usuario):
        """Cuenta cuántas valoraciones tiene un usuario."""
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM valoraciones WHERE id_usuario = ?", (str(id_usuario),))
            resultado = cursor.fetchone()
            if resultado:
                return resultado[0]
            return 0
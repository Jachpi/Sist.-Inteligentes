import sqlite3

class UsuarioModel:
    def __init__(self, db_path="peliculas.db"):
        self.db_path = db_path

    def conectar(self):
        """Establece conexión con la base de datos."""
        return sqlite3.connect(self.db_path)


    def insertar_usuario(self, nombre, correo, contrasena):
        """Inserta un nuevo usuario en la base de datos."""
        try:
            with self.conectar() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO usuario (nombre, correo_electronico, contrasena)
                    VALUES (?, ?, ?)
                """, (nombre, correo, contrasena))
                conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

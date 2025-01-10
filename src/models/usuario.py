import sqlite3
import hashlib

class UsuarioModel:
    def __init__(self, db_path="peliculas.db"):
        self.db_path = db_path

    def conectar(self):
        """Establece conexión con la base de datos."""
        return sqlite3.connect(self.db_path)


    def insertar_usuario(self, nombre, correo, contrasena):
        """Inserta un nuevo usuario en la base de datos."""
        contrasena_hash = self.encriptar_contrasena(contrasena)
        try:
            with self.conectar() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO usuario (nombre, correo_electronico, contrasena)
                    VALUES (?, ?, ?)
                """, (nombre, correo, contrasena_hash))
                conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False  # El correo ya está registrado

        
    def obtener_usuario_por_correo(self, correo):
        """Obtiene los datos de un usuario por su correo electrónico."""
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM usuario WHERE correo_electronico = ?
            """, (correo,))
            return cursor.fetchone()  # Retorna None si no existe

    def verificar_usuario(self, correo, contrasena):
        """Verifica si el usuario y la contraseña son correctos."""
        usuario = self.obtener_usuario_por_correo(correo)
        if usuario:
            contrasena_hash = self.encriptar_contrasena(contrasena)
            return usuario[3] == contrasena_hash  # Compara la contraseña encriptada
        return False

    def encriptar_contrasena(self, contrasena):
        """Encripta la contraseña usando SHA-256."""
        return hashlib.sha256(contrasena.encode()).hexdigest()

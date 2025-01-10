from PyQt5.QtWidgets import QMessageBox
from models.usuario import UsuarioModel
import hashlib

class LoginController:
    def __init__(self):
        self.modelo_usuario = UsuarioModel()

    def verificar_credenciales(self, correo, contrasena, parent=None):
        """
        Verifica las credenciales del usuario comparando con la base de datos.
        """
        if not correo or not contrasena:
            QMessageBox.warning(parent, "Error", "Todos los campos son obligatorios.")
            return False

        # Encriptar la contraseña para compararla con la almacenada
        contrasena_hash = self.encriptar_contrasena(contrasena)

        usuario = self.modelo_usuario.obtener_usuario_por_correo(correo)

        if usuario and usuario[3] == contrasena_hash:
            QMessageBox.information(parent, "Acceso permitido", f"¡Bienvenido {usuario[1]}!")
            return True
        else:
            QMessageBox.warning(parent, "Error", "Usuario o contraseña incorrectos.")
            return False

    def encriptar_contrasena(self, contrasena):
        """
        Encripta la contraseña usando SHA-256.
        """
        return hashlib.sha256(contrasena.encode()).hexdigest()

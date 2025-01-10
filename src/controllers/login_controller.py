from PyQt5.QtWidgets import QMessageBox
from models.usuario import UsuarioModel
from models.session import Sesion  # Importar la sesión
from view.menu import MenuDialog
import hashlib

class LoginController:
    def __init__(self):
        self.modelo_usuario = UsuarioModel()
        self.sesion = Sesion()

    def verificar_credenciales(self, correo, contrasena, ventana_login):
        if not correo or not contrasena:
            QMessageBox.warning(ventana_login, "Error", "Todos los campos son obligatorios.")
            return False

        usuario = self.modelo_usuario.obtener_usuario_por_correo(correo)

        if usuario and self.modelo_usuario.verificar_usuario(correo, contrasena):
            # Guardar sesión
            self.sesion.iniciar_sesion(usuario[0], usuario[1], usuario[2])  # id, nombre, correo

            # Cerrar login y abrir menú
            QMessageBox.information(ventana_login, "Acceso permitido", f"¡Bienvenido {usuario[1]}!")
            self.abrir_menu(ventana_login)
            return True
        else:
            QMessageBox.warning(ventana_login, "Error", "Usuario o contraseña incorrectos.")
            return False

    def abrir_menu(self, ventana_login):
        self.menu = MenuDialog()
        self.menu.show()
        ventana_login.close()



    def encriptar_contrasena(self, contrasena):
        """
        Encripta la contraseña usando SHA-256.
        """
        return hashlib.sha256(contrasena.encode()).hexdigest()

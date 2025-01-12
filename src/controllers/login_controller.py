from PyQt5.QtWidgets import QMessageBox
from models.usuario import UsuarioModel
from models.session import Sesion  # Importar la sesión
from view.menu import MenuDialog
import hashlib

class LoginController:
    def __init__(self):
        self.modelo_usuario = UsuarioModel()
        self.sesion = Sesion()

    def abrir_menu(self, ventana_login, id_usuario):
        self.menu = MenuDialog(id_usuario)
        self.menu.show()
        ventana_login.close()
        
    def verificar_credenciales(self, correo, contrasena):
        """Verifica si el usuario existe y devuelve su ID."""
        resultado = self.modelo_usuario.obtener_usuario(correo, contrasena)
        return resultado[0] if resultado else None

    def verificar_valoraciones_usuario(self, id_usuario):
        """Verifica cuántas valoraciones ha hecho el usuario."""
        return self.modelo_usuario.contar_valoraciones_usuario(id_usuario)



    def encriptar_contrasena(self, contrasena):
        """
        Encripta la contraseña usando SHA-256.
        """
        return hashlib.sha256(contrasena.encode()).hexdigest()

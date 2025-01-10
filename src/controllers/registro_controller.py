from PyQt5.QtWidgets import QMessageBox
from models.usuario import UsuarioModel

class RegistroController:
    def __init__(self):
        self.modelo_usuario = UsuarioModel()

    def registrar_usuario(self, nombre, correo, contrasena, parent=None):
        """Valida e inserta un usuario en la base de datos."""
        if not nombre or not correo or not contrasena:
            QMessageBox.warning(parent, "Error", "Todos los campos son obligatorios.")
            return False

        exito = self.modelo_usuario.insertar_usuario(nombre, correo, contrasena)

        if exito:
            QMessageBox.information(parent, "Registro Exitoso", f"Usuario '{nombre}' registrado correctamente.")
            return True
        else:
            QMessageBox.warning(parent, "Error", "El correo electrónico ya está registrado.")
            return False

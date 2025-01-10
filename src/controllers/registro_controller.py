from PyQt5.QtWidgets import QMessageBox
from views.registrar import RegistrarView
from models.user import User

class RegistroController:
    def __init__(self):
        self.view = RegistrarView()
        self.view.registrar_button.clicked.connect(self.registrar_usuario)

    def show(self):
        self.view.show()

    def registrar_usuario(self):
        usuario = self.view.usuario_input.text()
        contraseña = self.view.pass_input.text()

        if not usuario or not contraseña:
            QMessageBox.warning(self.view, "Error", "Todos los campos son obligatorios.")
            return

        if User.usuario_existente(usuario):
            QMessageBox.warning(self.view, "Error", "El usuario ya existe.")
            return

        User.registrar_usuario(usuario, contraseña)
        QMessageBox.information(self.view, "Éxito", f"Usuario '{usuario}' registrado correctamente.")
        self.view.close()
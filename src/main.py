from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from view.login import Ui_Dialog
from view.registrar import RegistrarDialog  # Importar la ventana de registro
import sys
import platform
import os

class LoginDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Conectar botones
        self.login.clicked.connect(self.verificar_credenciales)
        self.registrar.clicked.connect(self.abrir_ventana_registro)  # Conectar el botón de registro

    def verificar_credenciales(self):
        usuario = self.userInput.text()
        contraseña = self.passInput.text()

        if usuario == "admin" and contraseña == "1234":
            QMessageBox.information(self, "Acceso permitido", "¡Bienvenido!")
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos")

    def abrir_ventana_registro(self):
        self.ventana_registro = RegistrarDialog()
        self.ventana_registro.exec_()  # Mostrar la ventana de registro como diálogo modal

if __name__ == "__main__":
    if platform.system() == "Linux":
        os.environ["QT_QPA_PLATFORM"] = "xcb"
    elif platform.system() == "Windows":
        os.environ["QT_QPA_PLATFORM"] = "windows"
    elif platform.system() == "Darwin":
        os.environ["QT_QPA_PLATFORM"] = "cocoa"

    app = QApplication(sys.argv)
    ventana = LoginDialog()
    ventana.show()
    sys.exit(app.exec_())

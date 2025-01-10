from PyQt5.QtWidgets import QApplication
from view.login import LoginDialog
from view.registrar import RegistrarDialog  # Importar la ventana de registro
import sys
import platform
import os

if __name__ == "__main__":
    if platform.system() == "Linux":
        os.environ["QT_QPA_PLATFORM"] = "xcb"
    elif platform.system() == "Windows":
        os.environ["QT_QPA_PLATFORM"] = "windows"
    elif platform.system() == "Darwin":
        os.environ["QT_QPA_PLATFORM"] = "cocoa"

    app = QApplication(sys.argv)
    ventana = LoginDialog()  # Instanciar directamente LoginDialog
    ventana.show()
    sys.exit(app.exec_())
